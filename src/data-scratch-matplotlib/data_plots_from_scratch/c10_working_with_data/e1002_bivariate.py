from matplotlib import pyplot as plt

from dsl.c05_statistics.e0503_correlation import correlation
from dsl.c10_working_with_data.e1002_bivariate import random_normal

xs = [random_normal() for _ in range(1000)]
ys1 = [x + random_normal() / 2 for x in xs]
ys2 = [-x + random_normal() / 2 for x in xs]
plt.scatter(xs, ys1, marker='.', color='black', label='ys1')
plt.scatter(xs, ys2, marker='.', color='gray', label='ys2')
plt.xlabel('xs')
plt.ylabel('ys')
plt.legend(loc=9)
plt.title("Very Different Joint Distributions")
plt.show()

print(correlation(xs, ys1))  # about 0.9
print(correlation(xs, ys2))  # about -0.9
