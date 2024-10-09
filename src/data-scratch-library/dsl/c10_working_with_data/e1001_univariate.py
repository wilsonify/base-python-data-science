import math
from collections import Counter
from typing import List


def bucketize(point: float, bucket_size: float) -> float:
    """
    Floor the point to the next lower multiple of bucket_size.

    Args:
        point (float): The value to bucketize.
        bucket_size (float): The size of each bucket.

    Returns:
        float: The bucketized value.
    """
    return bucket_size * math.floor(point / bucket_size)


def make_histogram(points: List[float], bucket_size: float) -> Counter:
    """
    Buckets the points and counts how many fall into each bucket.

    Args:
        points (List[float]): A list of points to be bucketized.
        bucket_size (float): The size of each bucket.

    Returns:
        Counter: A Counter object where the keys are the bucketized values
                 and the values are the counts.
    """
    return Counter(bucketize(point, bucket_size) for point in points)


