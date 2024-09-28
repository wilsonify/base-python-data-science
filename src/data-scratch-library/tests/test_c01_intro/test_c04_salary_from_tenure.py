from dsl.c01_intro.c04_salary_from_tenure import SalaryTenure


def test_tenure_bucket():
    # Test cases for tenure_bucket method
    salary_tenure1 = SalaryTenure(salary=50000, tenure=1.5)
    assert salary_tenure1.tenure_bucket() == "less than two"

    salary_tenure2 = SalaryTenure(salary=60000, tenure=3.0)
    assert salary_tenure2.tenure_bucket() == "between two and five"

    salary_tenure3 = SalaryTenure(salary=70000, tenure=5.0)
    assert salary_tenure3.tenure_bucket() == "more than five"

    salary_tenure4 = SalaryTenure(salary=80000, tenure=10.0)
    assert salary_tenure4.tenure_bucket() == "more than five"


def test_predict_paid_or_unpaid():
    # Test cases for predict_paid_or_unpaid method
    salary_tenure1 = SalaryTenure(salary=50000, tenure=2.5)
    assert salary_tenure1.predict_paid_or_unpaid() == "paid"

    salary_tenure2 = SalaryTenure(salary=60000, tenure=6.0)
    assert salary_tenure2.predict_paid_or_unpaid() == "unpaid"

    salary_tenure3 = SalaryTenure(salary=70000, tenure=8.0)
    assert salary_tenure3.predict_paid_or_unpaid() == "unpaid"

    salary_tenure4 = SalaryTenure(salary=80000, tenure=9.0)
    assert salary_tenure4.predict_paid_or_unpaid() == "paid"

    salary_tenure5 = SalaryTenure(salary=90000, tenure=10.0)
    assert salary_tenure5.predict_paid_or_unpaid() == "paid"
