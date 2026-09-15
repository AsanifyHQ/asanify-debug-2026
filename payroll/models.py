"""In-memory record types. A real deployment reads these from MySQL."""

from dataclasses import dataclass, field
from decimal import Decimal
from typing import List


@dataclass(frozen=True)
class Component:
    code: str
    amount: Decimal


@dataclass(frozen=True)
class Payslip:
    payslip_id: str
    company_id: str
    period_id: str
    employee_name: str
    joined_on: str
    components: List[Component] = field(default_factory=list)
