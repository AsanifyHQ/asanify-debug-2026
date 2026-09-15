"""Payslip lookup. Every read is scoped to one company."""


class PayslipStore:
    def __init__(self, rows):
        self._rows = list(rows)

    def list_payslips(self, company_id, period_id=None):
        """Payslips belonging to `company_id`.

        When `period_id` is given the result is narrowed to that payroll run.
        """
        if period_id is not None:
            rows = [r for r in self._rows if r.period_id == period_id]
        else:
            rows = list(self._rows)
            rows = [r for r in rows if r.company_id == company_id]
        return rows

    def get_payslip(self, company_id, payslip_id):
        for row in self._rows:
            if row.payslip_id == payslip_id and row.company_id == company_id:
                return row
        return None
