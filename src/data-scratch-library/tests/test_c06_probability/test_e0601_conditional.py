from random import seed

from dsl.c06_probability.e0601_conditional import Kid, random_kid, simulate


def test_kid_enum():
    """Test the Kid Enum values."""
    assert Kid.BOY.value == "boy"
    assert Kid.GIRL.value == "girl"
    assert Kid.BOY.name == "BOY"
    assert Kid.GIRL.name == "GIRL"


def test_random_kid_set():
    result = random_kid()
    # Use a set of Kid Enum values
    expected = {Kid.BOY, Kid.GIRL}
    assert result in expected


def test_random_kid():
    """Test that random_kid returns a valid Kid Enum."""
    seed(0)  # Set seed for reproducibility
    results = [random_kid() for _ in range(1000)]
    assert all(isinstance(kid, Kid) for kid in results)  # All results should be instances of Kid Enum
    assert results.count(Kid.BOY) + results.count(Kid.GIRL) == 1000  # Should sum up to 1000


def test_simulate():
    """Test the simulate function's return values."""
    # Run the simulation
    both_girls_given_either, both_girls_given_older = simulate()

    # Check if the returned values are within the expected range
    assert 0 <= both_girls_given_either <= 1
    assert 0 <= both_girls_given_older <= 1

    # These values are expected based on the problem's probabilities
    # Update these values according to your simulation expectations
    expected_both_girls_given_either = 0.3333  # Update based on expectations
    expected_both_girls_given_older = 0.5  # Update based on expectations

    eps = 0.01
    assert abs(both_girls_given_either - expected_both_girls_given_either) < eps
    assert abs(both_girls_given_older - expected_both_girls_given_older) < eps
