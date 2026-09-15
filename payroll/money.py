"""Money helpers. All amounts are Decimal rupees."""

from decimal import Decimal, ROUND_HALF_UP

PAISE = Decimal("0.01")


def round_money(amount):
    """Round a rupee amount to the nearest paisa."""
    return Decimal(amount).quantize(PAISE, rounding=ROUND_HALF_UP)


def total_earnings(components):
    """Sum the earning components of a single payslip.

    `components` is an iterable of objects with an `.amount` Decimal.
    """
    total = Decimal("0")
    for component in components:
        total += round_money(component.amount)
    return round_money(total)
