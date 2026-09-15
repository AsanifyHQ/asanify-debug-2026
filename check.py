#!/usr/bin/env python3
"""No-install fallback. The same four tickets as the test suite, stdlib only.

    python3 check.py

Use this if `pip install` will not work on your machine or your network.
It is not a substitute for reading tests/test_payroll.py -- the tests carry the
reports themselves, which is where the useful detail is. This just tells you
which of the four currently pass.
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


def ticket_4471():
    from payroll.service import run_summary
    from payroll.store import PayslipStore
    s = run_summary(PayslipStore([]), "acme", "JAN-2026", 2026, 1)
    assert s["headcount"] == 0, s
    assert s["total_gross"] == Decimal("0.00"), s
    assert s["highest_gross"] == Decimal("0.00"), s


def ticket_4488():
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


def ticket_4502():
    from payroll.periods import days_worked, period_bounds
    start, end = period_bounds(2026, 1)
    got = days_worked("2026-01-16T00:00:00+05:30", start, end)
    assert got == 16, got


def ticket_4515():
    from payroll.models import Component
    from payroll.money import total_earnings
    items = [Component(code=f"C{i}", amount=Decimal("12500.004")) for i in range(4)]
    got = total_earnings(items)
    assert got == Decimal("50000.02"), got


if __name__ == "__main__":
    check("TICKET 4471  report before the first payroll", ticket_4471)
    check("TICKET 4488  January report for ACME", ticket_4488)
    check("TICKET 4502  report with an imported joining date", ticket_4502)
    check("TICKET 4515  January register totals", ticket_4515)

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
