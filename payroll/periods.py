"""Payroll period arithmetic."""

import calendar
from datetime import datetime


def period_bounds(year, month):
    """Return the first and last instant of a payroll month."""
    last_day = calendar.monthrange(year, month)[1]
    return (
        datetime(year, month, 1, 0, 0, 0),
        datetime(year, month, last_day, 23, 59, 59),
    )


def parse_joining_date(raw):
    """Joining dates arrive as ISO 8601 strings from the employee importer.

    Some sources send a UTC offset, some do not.
    """
    return datetime.fromisoformat(raw)


def days_worked(joined_on, period_start, period_end):
    """Days the employee was on the payroll during this period."""
    joined = parse_joining_date(joined_on)
    if joined <= period_start:
        return (period_end - period_start).days + 1
    return (period_end - joined).days + 1


def proration_factor(joined_on, year, month):
    """Fraction of the month the employee actually worked."""
    period_start, period_end = period_bounds(year, month)
    worked = days_worked(joined_on, period_start, period_end)
    in_month = calendar.monthrange(year, month)[1]
    return min(worked, in_month) / in_month
