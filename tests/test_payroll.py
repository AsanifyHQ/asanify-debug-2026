"""The four cases support has raised this month.

Each one is a real bug report. None of them tells you where the defect is.
"""

from decimal import Decimal

from payroll.models import Component
from payroll.money import total_earnings
from payroll.periods import days_worked, period_bounds
from payroll.service import run_summary
from payroll.store import PayslipStore


def test_summary_of_a_run_with_no_payslips():
    """A company opens the report before anyone has been paid.

    Reported as: "the page 500s for our new entity".
    """
    empty = PayslipStore([])

    summary = run_summary(empty, "acme", "JAN-2026", 2026, 1)

    assert summary["headcount"] == 0
    assert summary["total_gross"] == Decimal("0.00")
    assert summary["highest_gross"] == Decimal("0.00")


def test_summary_covers_only_the_requesting_company(two_companies):
    """ACME's admin opens the January report.

    Reported as: "our headcount is wrong and I don't recognise the total".
    """
    summary = run_summary(two_companies, "acme", "JAN-2026", 2026, 1)

    assert summary["headcount"] == 2
    assert summary["total_gross"] == Decimal("100000.00")


def test_employee_who_joined_mid_month_is_prorated():
    """The importer sends this employee's joining date with a +05:30 offset.

    Reported as: "payroll won't finish for the January batch".
    """
    period_start, period_end = period_bounds(2026, 1)

    worked = days_worked("2026-01-16T00:00:00+05:30", period_start, period_end)

    assert worked == 16


def test_payslip_total_is_rounded_once():
    """Statutory rule: components are carried at full precision and the
    payslip total is rounded to the nearest paisa exactly once.

    Reported as: "our total is a few paise off the register every month".
    """
    components = [Component(code=f"C{i}", amount=Decimal("12500.004")) for i in range(4)]

    assert total_earnings(components) == Decimal("50000.02")
