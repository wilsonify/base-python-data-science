from random import seed

from dsl.c10_working_with_data.e1001_univariate import make_histogram, bucketize


def test_bucketize():
    assert bucketize(42, 10) == 40
    assert bucketize(59, 10) == 50
    assert bucketize(61, 10) == 60
    assert bucketize(99, 25) == 75
    assert bucketize(101, 50) == 100


def test_make_histogram():
    seed(0)
    points = [5, 15, 25, 35, 45, 55]
    bucket_size = 10
    histogram = make_histogram(points, bucket_size)
    assert len(histogram) == 6

    points = [1, 5, 10, 20, 25, 30]
    bucket_size = 5
    histogram = make_histogram(points, bucket_size)
    assert len(histogram) == 6
