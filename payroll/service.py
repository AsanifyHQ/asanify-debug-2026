"""Payroll run reporting."""

from decimal import Decimal

from payroll.money import round_money, total_earnings
from payroll.periods import proration_factor


def gross_for(payslip, year, month):
    """Prorated gross pay for one payslip."""
    full = total_earnings(payslip.components)
    factor = proration_factor(payslip.joined_on, year, month)
    return round_money(full * Decimal(str(factor)))


def run_summary(store, company_id, period_id, year, month):
    """Headline numbers a payroll admin sees after a run completes."""
    payslips = store.list_payslips(company_id, period_id)
    grosses = [gross_for(p, year, month) for p in payslips]

    highest = max(grosses)
    total = sum(grosses, Decimal("0"))

    return {
        "company_id": company_id,
        "period_id": period_id,
        "headcount": len(payslips),
        "total_gross": round_money(total),
        "highest_gross": round_money(highest),
    }
