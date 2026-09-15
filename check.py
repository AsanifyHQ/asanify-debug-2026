#!/usr/bin/env python3
"""No-install fallback. Same four checks as the test suite, stdlib only.

    python3 check.py

Use this if `pip install` will not work on your machine or your network.
It is not a substitute for reading tests/test_payroll.py -- the tests carry the
bug reports and the expected values. This just tells you which ones pass.
"""

from decimal import Decimal

RESULTS = []


def check(name, fn):
    try:
        fn()
    except Exception as exc:
        RESULTS.append((name, f"{type(exc).__name__}: {exc}"))
    else:
        RESULTS.append((name, None))


def one_empty_run():
    from payroll.service import run_summary
    from payroll.store import PayslipStore
    s = run_summary(PayslipStore([]), "acme", "JAN-2026", 2026, 1)
    assert s["headcount"] == 0, s
    assert s["total_gross"] == Decimal("0.00"), s
    assert s["highest_gross"] == Decimal("0.00"), s


def two_company_scoped():
    from payroll.models import Component, Payslip
    from payroll.service import run_summary
    from payroll.store import PayslipStore
    def slip(pid, company, name):
        return Payslip(payslip_id=pid, company_id=company, period_id="JAN-2026",
                       employee_name=name, joined_on="2026-01-01T00:00:00",
                       components=[Component(code="BASIC", amount=Decimal("50000.00"))])
    store = PayslipStore([slip("ps-1", "acme", "Riya"), slip("ps-2", "acme", "Arjun"),
                          slip("ps-3", "globex", "Sneha")])
    s = run_summary(store, "acme", "JAN-2026", 2026, 1)
    assert s["headcount"] == 2, s
    assert s["total_gross"] == Decimal("100000.00"), s


def three_offset_joining_date():
    from payroll.periods import days_worked, period_bounds
    start, end = period_bounds(2026, 1)
    got = days_worked("2026-01-16T00:00:00+05:30", start, end)
    assert got == 16, got


def four_rounded_once():
    from payroll.models import Component
    from payroll.money import total_earnings
    items = [Component(code=f"C{i}", amount=Decimal("12500.004")) for i in range(4)]
    got = total_earnings(items)
    assert got == Decimal("50000.02"), got


if __name__ == "__main__":
    check("1  summary of a run with no payslips", one_empty_run)
    check("2  summary covers only the requesting company", two_company_scoped)
    check("3  employee who joined mid-month is prorated", three_offset_joining_date)
    check("4  payslip total is rounded once", four_rounded_once)

    width = max(len(n) for n, _ in RESULTS)
    failed = 0
    print()
    for name, err in RESULTS:
        if err is None:
            print(f"  PASS  {name}")
        else:
            failed += 1
            print(f"  FAIL  {name.ljust(width)}   {err}")
    print(f"\n  {len(RESULTS) - failed} passing, {failed} failing\n")
    raise SystemExit(1 if failed else 0)
