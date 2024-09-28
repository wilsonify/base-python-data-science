def uniform_pdf(x, a=0, b=1):
    assert b > a, "maximum,b, must be greater than minimum,a"
    return 1 / (b - a) if a <= x < b else 0


def uniform_cdf(x, a=0, b=1):
    """returns the probability that a uniform random variable is less than x"""
    if x < a:
        return 0
    if a < x < b:
        return (x - a) / (b - a)  # e.g. P(X < 0.4) = 0.4
    if b <= x:
        return 1
