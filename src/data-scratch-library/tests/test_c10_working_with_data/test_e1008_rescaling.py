from dsl.c10_working_with_data.e1008_rescaling import scale, rescale


def test_rescaling():
    """Test rescaling of vectors."""
    vectors = [[-3, -1, 1], [-1, 0, 1], [1, 1, 1]]

    # Test scale function
    means, stdevs = scale(vectors)
    assert means == [-1, 0, 1]
    assert stdevs == [2, 1, 0]

    # Test rescale function
    rescaled = rescale(vectors)
    new_means, new_stdevs = scale(rescaled)
    assert new_means == [0, 0, 1]
    assert new_stdevs == [1, 1, 0]
