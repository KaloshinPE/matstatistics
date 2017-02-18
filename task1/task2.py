import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import factorial

N = 10**4
theta = 1

sample = theta*np.random.exponential(theta, N)


def estimation(n, k):
    return (float(factorial(k))/(sum(map(lambda x: x**k, sample[:n]))/float(n)))**(1.0/k)


k_row = range(11)[1:]
k_row = map(lambda x: x**2, k_row)
est_rows = []
est_labels = []
for k in k_row:
    new_row = []
    for n in range(N)[1:]:
         new_row.append(np.abs(estimation(n, k) - theta))
    est_rows.append(new_row)
    est_labels.append(str(k))

for i in range(len(k_row)):
    plt.plot(range(N)[1:], est_rows[i], label=est_labels[i])
plt.legend()
plt.show()

