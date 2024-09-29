from dsl.c06_probability.e0603_normal import random_normal


def random_matrix():
    num_points = 100
    data = []
    for _ in range(num_points):
        row = [None, None, None, None]
        row[0] = random_normal()
        row[1] = -5 * row[0] + random_normal()
        row[2] = row[0] + row[1] + 5 * random_normal()
        row[3] = 6 if row[2] > -2 else 0
        data.append(row)
    return data
