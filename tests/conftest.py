from decimal import Decimal

import pytest

from payroll.models import Component, Payslip
from payroll.store import PayslipStore


def slip(payslip_id, company_id, name, joined_on="2026-01-01T00:00:00", basic="50000.00"):
    return Payslip(
        payslip_id=payslip_id,
        company_id=company_id,
        period_id="JAN-2026",
        employee_name=name,
        joined_on=joined_on,
        components=[Component(code="BASIC", amount=Decimal(basic))],
    )


@pytest.fixture
def two_companies():
    """ACME has two employees this month. GLOBEX has one. Same period."""
    return PayslipStore([
        slip("ps-1", "acme", "Riya"),
        slip("ps-2", "acme", "Arjun"),
        slip("ps-3", "globex", "Sneha"),
    ])
