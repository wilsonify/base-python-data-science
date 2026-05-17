import math
import pytest

from dsl.c16_logistic_regression.logistic_regression import (
    logistic,
    logistic_prime,
    logistic_log_likelihood_i,
    logistic_log_likelihood,
    logistic_log_partial_ij,
    logistic_log_gradient_i,
    logistic_log_gradient,
    score_logistic,
)


# ---------------------------------------------------------------------------
# logistic (sigmoid)
# ---------------------------------------------------------------------------
class TestLogistic:
    def test_zero(self):
        assert logistic(0) == 0.5

    def test_large_positive(self):
        assert logistic(1000) == 1.0

    def test_large_negative(self):
        assert logistic(-1000) == 0.0

    def test_overflow_boundary(self):
        assert logistic(710) == 1.0

    def test_underflow_boundary(self):
        assert logistic(-710) == 0.0

    def test_positive_value(self):
        expected = 1.0 / (1 + math.exp(-1))
        assert logistic(1) == pytest.approx(expected)

    def test_negative_value(self):
        expected = 1.0 / (1 + math.exp(1))
        assert logistic(-1) == pytest.approx(expected)

    def test_symmetry(self):
        """logistic(x) + logistic(-x) == 1"""
        for x in [0.5, 1, 2, 5, 100]:
            assert logistic(x) + logistic(-x) == pytest.approx(1.0)

    def test_output_range(self):
        for x in [-500, -10, -1, 0, 1, 10, 500]:
            assert 0.0 <= logistic(x) <= 1.0


# ---------------------------------------------------------------------------
# logistic_prime
# ---------------------------------------------------------------------------
class TestLogisticPrime:
    def test_at_zero(self):
        assert logistic_prime(0) == pytest.approx(0.25)

    def test_positive(self):
        s = logistic(2)
        assert logistic_prime(2) == pytest.approx(s * (1 - s))

    def test_large_values_near_zero(self):
        assert logistic_prime(100) == pytest.approx(0.0, abs=1e-30)
        assert logistic_prime(-100) == pytest.approx(0.0, abs=1e-30)


# ---------------------------------------------------------------------------
# logistic_log_likelihood_i
# ---------------------------------------------------------------------------
class TestLogisticLogLikelihoodI:
    def test_positive_label(self):
        x_i = [1, 2]
        beta = [0, 0]
        # logistic(dot([1,2],[0,0])) = logistic(0) = 0.5
        expected = math.log(0.5)
        assert logistic_log_likelihood_i(x_i, 1, beta) == pytest.approx(expected)

    def test_negative_label(self):
        x_i = [1, 2]
        beta = [0, 0]
        expected = math.log(1 - 0.5)
        assert logistic_log_likelihood_i(x_i, 0, beta) == pytest.approx(expected)

    def test_high_confidence_positive(self):
        x_i = [1, 1]
        beta = [10, 10]
        # dot = 20, logistic(20) ≈ 1, log(1) ≈ 0
        result = logistic_log_likelihood_i(x_i, 1, beta)
        assert result == pytest.approx(0.0, abs=1e-6)

    def test_high_confidence_negative(self):
        x_i = [1, 1]
        beta = [-10, -10]
        # dot = -20, logistic(-20) ≈ 0, log(1-0) ≈ 0
        result = logistic_log_likelihood_i(x_i, 0, beta)
        assert result == pytest.approx(0.0, abs=1e-6)


# ---------------------------------------------------------------------------
# logistic_log_likelihood
# ---------------------------------------------------------------------------
class TestLogisticLogLikelihood:
    def test_sum_of_individuals(self):
        x = [[1, 0], [0, 1], [1, 1]]
        y = [1, 0, 1]
        beta = [0.5, -0.5]
        total = logistic_log_likelihood(x, y, beta)
        individual_sum = sum(
            logistic_log_likelihood_i(x_i, y_i, beta) for x_i, y_i in zip(x, y)
        )
        assert total == pytest.approx(individual_sum)

    def test_all_zero_beta(self):
        x = [[1, 2], [3, 4]]
        y = [1, 0]
        beta = [0, 0]
        # Each point contributes log(0.5)
        expected = 2 * math.log(0.5)
        assert logistic_log_likelihood(x, y, beta) == pytest.approx(expected)

    def test_likelihood_is_negative(self):
        x = [[1, 0], [0, 1]]
        y = [1, 0]
        beta = [1, 1]
        assert logistic_log_likelihood(x, y, beta) < 0


# ---------------------------------------------------------------------------
# logistic_log_partial_ij
# ---------------------------------------------------------------------------
class TestLogisticLogPartialIJ:
    def test_zero_beta(self):
        x_i = [1, 2]
        beta = [0, 0]
        # (y_i - logistic(0)) * x_i[j] = (1 - 0.5) * 1 = 0.5
        assert logistic_log_partial_ij(x_i, 1, beta, 0) == pytest.approx(0.5)
        # j=1: (1 - 0.5) * 2 = 1.0
        assert logistic_log_partial_ij(x_i, 1, beta, 1) == pytest.approx(1.0)

    def test_negative_label(self):
        x_i = [1, 3]
        beta = [0, 0]
        # (0 - 0.5) * 1 = -0.5
        assert logistic_log_partial_ij(x_i, 0, beta, 0) == pytest.approx(-0.5)
        # (0 - 0.5) * 3 = -1.5
        assert logistic_log_partial_ij(x_i, 0, beta, 1) == pytest.approx(-1.5)


# ---------------------------------------------------------------------------
# logistic_log_gradient_i
# ---------------------------------------------------------------------------
class TestLogisticLogGradientI:
    def test_length_matches_beta(self):
        x_i = [1, 2, 3]
        beta = [0, 0, 0]
        grad = logistic_log_gradient_i(x_i, 1, beta)
        assert len(grad) == len(beta)

    def test_values_match_partials(self):
        x_i = [1, 2]
        beta = [0.3, -0.7]
        y_i = 1
        grad = logistic_log_gradient_i(x_i, y_i, beta)
        for j in range(len(beta)):
            expected = logistic_log_partial_ij(x_i, y_i, beta, j)
            assert grad[j] == pytest.approx(expected)

    def test_zero_beta_positive_label(self):
        x_i = [1, 2]
        beta = [0, 0]
        grad = logistic_log_gradient_i(x_i, 1, beta)
        assert grad[0] == pytest.approx(0.5)
        assert grad[1] == pytest.approx(1.0)


# ---------------------------------------------------------------------------
# logistic_log_gradient
# ---------------------------------------------------------------------------
class TestLogisticLogGradient:
    def test_single_point_matches_gradient_i(self):
        x = [[1, 2]]
        y = [1]
        beta = [0.5, -0.5]
        full = logistic_log_gradient(x, y, beta)
        single = logistic_log_gradient_i(x[0], y[0], beta)
        for a, b in zip(full, single):
            assert a == pytest.approx(b)

    def test_multiple_points(self):
        x = [[1, 0], [0, 1]]
        y = [1, 0]
        beta = [0, 0]
        grad = logistic_log_gradient(x, y, beta)
        # Point 1: (1 - 0.5)*[1,0] = [0.5, 0]
        # Point 2: (0 - 0.5)*[0,1] = [0, -0.5]
        # Sum: [0.5, -0.5]
        assert grad[0] == pytest.approx(0.5)
        assert grad[1] == pytest.approx(-0.5)

    def test_gradient_length(self):
        x = [[1, 2, 3], [4, 5, 6]]
        y = [1, 0]
        beta = [0, 0, 0]
        grad = logistic_log_gradient(x, y, beta)
        assert len(grad) == 3


# ---------------------------------------------------------------------------
# score_logistic
# ---------------------------------------------------------------------------
class TestScoreLogistic:
    def test_perfect_prediction(self):
        # beta_hat such that dot(beta, x) > 0 for positives, < 0 for negatives
        beta_hat = [10, 0]
        x_test = [[1, 0], [1, 0], [-1, 0], [-1, 0]]
        y_test = [1, 1, 0, 0]
        precision, recall = score_logistic(beta_hat, x_test, y_test)
        assert precision == pytest.approx(1.0)
        assert recall == pytest.approx(1.0)

    def test_known_confusion_matrix(self):
        # Construct: TP=2, FP=1, FN=1, TN=1
        # beta_hat = [10, 0]: predict positive when x[0]>0, negative when x[0]<0
        beta_hat = [10, 0]
        x_test = [
            [1, 0],   # predict 1, actual 1 -> TP
            [1, 0],   # predict 1, actual 1 -> TP
            [1, 0],   # predict 1, actual 0 -> FP
            [-1, 0],  # predict 0, actual 1 -> FN
            [-1, 0],  # predict 0, actual 0 -> TN
        ]
        y_test = [1, 1, 0, 1, 0]
        precision, recall = score_logistic(beta_hat, x_test, y_test)
        # precision = TP/(TP+FP) = 2/3
        assert precision == pytest.approx(2.0 / 3.0)
        # recall = TP/(TP+FN) = 2/3
        assert recall == pytest.approx(2.0 / 3.0)

    def test_all_positive_predictions(self):
        beta_hat = [10, 0]
        x_test = [[1, 0], [1, 0], [1, 0]]
        y_test = [1, 1, 0]
        precision, recall = score_logistic(beta_hat, x_test, y_test)
        # TP=2, FP=1, FN=0 => precision=2/3, recall=1.0
        assert precision == pytest.approx(2.0 / 3.0)
        assert recall == pytest.approx(1.0)
