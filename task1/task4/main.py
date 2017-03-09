import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

N = 10**4
sample = np.random.normal(size=N)
x_row = np.linspace(-5, 5, 1000)


def emp_funk(n):
    print n
    funk = []
    data = list(np.flipud(np.sort(sample[:n])))
    for x in enumerate(x_row):
        if funk:
            funk.append(funk[-1])
        else:
            funk.append(0)
        while data:
            if x[1] < data[-1]:
                break
            funk[-1] += 1
            del data[-1]
    return np.array(funk)/float(n)


n_row = [10, 25, 50, 100, 1000]
real_funk = norm.cdf(x_row)
'''for n in n_row:
    plt.plot(x_row, emp_funk(n), label=str(n))
    plt.plot(x_row, real_funk, label='true')
    plt.scatter(sample[:n], np.zeros(n), alpha=0.2, label='data')
    plt.legend()
    plt.show()
'''

D_row = [max(np.abs(real_funk-emp_funk(n))) for n in range(N)[1:]]
plt.subplot(121)
plt.plot(range(N)[1:], D_row)
plt.subplot(122)
plt.plot(range(N)[1:], [D_row[i-1]*np.sqrt(i) for i in range(N)[1:]])
plt.show()