from dataclasses import dataclass


@dataclass
class SalaryTenure:
    salary: int
    tenure: float

    def tenure_bucket(self):
        if self.tenure < 2:
            return "less than two"
        elif self.tenure < 5:
            return "between two and five"
        else:
            return "more than five"

    def predict_paid_or_unpaid(self):
        if self.tenure < 3.0:
            return "paid"
        elif self.tenure < 8.5:
            return "unpaid"
        else:
            return "paid"
