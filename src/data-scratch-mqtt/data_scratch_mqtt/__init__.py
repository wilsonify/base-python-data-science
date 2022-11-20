from data_scratch_mqtt.config import MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE
from data_scratch_mqtt.strategies_library.abstract import Strategy
from data_scratch_mqtt.strategies_library.echo import echo_strategy
from data_scratch_mqtt.strategies_library.gradient_descent import difference_quotient
from data_scratch_mqtt.strategies_library.gradient_descent import estimate_gradient
from data_scratch_mqtt.strategies_library.gradient_descent import in_random_order
from data_scratch_mqtt.strategies_library.gradient_descent import maximize_batch
from data_scratch_mqtt.strategies_library.gradient_descent import maximize_stochastic
from data_scratch_mqtt.strategies_library.gradient_descent import minimize_batch
from data_scratch_mqtt.strategies_library.gradient_descent import minimize_stochastic
from data_scratch_mqtt.strategies_library.gradient_descent import partial_difference_quotient
from data_scratch_mqtt.strategies_library.linear_algebra import distance
from data_scratch_mqtt.strategies_library.linear_algebra import dot
from data_scratch_mqtt.strategies_library.linear_algebra import get_column
from data_scratch_mqtt.strategies_library.linear_algebra import get_row
from data_scratch_mqtt.strategies_library.linear_algebra import magnitude
from data_scratch_mqtt.strategies_library.linear_algebra import matrix_add
from data_scratch_mqtt.strategies_library.linear_algebra import scalar_multiply
from data_scratch_mqtt.strategies_library.linear_algebra import shape
from data_scratch_mqtt.strategies_library.linear_algebra import squared_distance
from data_scratch_mqtt.strategies_library.linear_algebra import sum_of_squares
from data_scratch_mqtt.strategies_library.linear_algebra import vector_add
from data_scratch_mqtt.strategies_library.linear_algebra import vector_mean
from data_scratch_mqtt.strategies_library.linear_algebra import vector_subtract
from data_scratch_mqtt.strategies_library.linear_algebra import vector_sum
from data_scratch_mqtt.strategies_library.machine_learning import accuracy
from data_scratch_mqtt.strategies_library.machine_learning import f1_score
from data_scratch_mqtt.strategies_library.machine_learning import precision
from data_scratch_mqtt.strategies_library.machine_learning import recall
from data_scratch_mqtt.strategies_library.machine_learning import split_data
from data_scratch_mqtt.strategies_library.machine_learning import train_test_split
from data_scratch_mqtt.strategies_library.mysqrt import mysqrt_strategy
from data_scratch_mqtt.strategies_library.mystrength import mystrength_strategy
from data_scratch_mqtt.strategies_library.probability import bernoulli_trial
from data_scratch_mqtt.strategies_library.probability import binomial
from data_scratch_mqtt.strategies_library.probability import inverse_normal_cdf
from data_scratch_mqtt.strategies_library.probability import normal_cdf
from data_scratch_mqtt.strategies_library.probability import normal_pdf
from data_scratch_mqtt.strategies_library.probability import random_kid
from data_scratch_mqtt.strategies_library.probability import uniform_cdf
from data_scratch_mqtt.strategies_library.probability import uniform_pdf
from data_scratch_mqtt.strategies_library.stats import bucketize
from data_scratch_mqtt.strategies_library.stats import correlation
from data_scratch_mqtt.strategies_library.stats import correlation_matrix
from data_scratch_mqtt.strategies_library.stats import covariance
from data_scratch_mqtt.strategies_library.stats import data_range
from data_scratch_mqtt.strategies_library.stats import de_mean
from data_scratch_mqtt.strategies_library.stats import interquartile_range
from data_scratch_mqtt.strategies_library.stats import mean
from data_scratch_mqtt.strategies_library.stats import median
from data_scratch_mqtt.strategies_library.stats import mode
from data_scratch_mqtt.strategies_library.stats import quantile
from data_scratch_mqtt.strategies_library.stats import standard_deviation
from data_scratch_mqtt.strategies_library.stats import variance
