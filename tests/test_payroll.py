"""Four tickets support raised this month.

Each docstring is the report as it came in. Each test is what the reporter
expected to see. Neither tells you which line is at fault -- that part is the
job.
"""

from decimal import Decimal

from payroll.models import Component
from payroll.money import total_earnings
from payroll.periods import days_worked, period_bounds
from payroll.service import run_summary
from payroll.store import PayslipStore


def test_report_before_the_first_payroll():
    """TICKET 4471, from an admin at a company that onboarded last week:

    "I clicked into the January report and the page just died. We have not run
    payroll yet, so maybe that is why, but it should not break."
    """
    summary = run_summary(PayslipStore([]), "acme", "JAN-2026", 2026, 1)

    assert summary["headcount"] == 0
    assert summary["total_gross"] == Decimal("0.00")
    assert summary["highest_gross"] == Decimal("0.00")


def test_january_report_for_acme(january):
    """TICKET 4488, from ACME's payroll admin:

    "Our January report says we have more people on it than we employ, and the
    total does not match what we approved. We have two employees this month."
    """
    summary = run_summary(january, "acme", "JAN-2026", 2026, 1)

    assert summary["headcount"] == 2
    assert summary["total_gross"] == Decimal("100000.00")


def test_report_with_an_imported_joining_date():
    """TICKET 4502, from support, after an employee import:

    "January will not finish for this customer at all. It falls over every time.
    The only thing unusual is one employee who joined on the 16th and came in
    through the importer."

    That importer sends joining dates with a +05:30 offset on them.
    """
    period_start, period_end = period_bounds(2026, 1)

    assert days_worked("2026-01-16T00:00:00+05:30", period_start, period_end) == 16


def test_january_register_totals():
    """TICKET 4515, from finance:

    "Every month we are a few paise away from the register. It is small but it
    never nets out, and at our headcount it adds up."

    Finance's rule, for reference: components are carried at full precision and
    the payslip total is rounded to the nearest paisa exactly once.
    """
    components = [Component(code=f"C{i}", amount=Decimal("12500.004")) for i in range(4)]

    assert total_earnings(components) == Decimal("50000.02")
