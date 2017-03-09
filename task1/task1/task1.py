import numpy as np
import matplotlib.pyplot as plt

N = 10**4
theta = 5

sample = theta*np.random.rand(N)


def est0(n):
    return 2*sum(sample[:n])/float(n)


def est1(n):
    return est0(n)*0.5 + sample[n-1]*0.5


def est2(n):
    return (n+1)*sample[0]


def est3(n):
    return sample[0] + sample[n-1]


def est4(n):
    return (n+1)/float(n)*sample[n-1]

est_rows = [[],[],[],[],[]]
est_functions = [est0, est1, est2, est3, est4]
est_colors = ['r', 'g', 'b', 'y', 'm']
est_labels = ['2$\overline{X}$', '$\overline{X} + {X_{n}}/{2}$', '(n+1)$X_1$', '$X_1 + X_n$', '${n+1}/{n}X_n$']
for n in range(N)[1:]:
    for i in range(5):
        est_rows[i].append(np.abs(est_functions[i](n) - theta))

for i in range(5):
    plt.plot(range(N)[1:], est_rows[i], color=est_colors[i], label=est_labels[i])
plt.legend()
plt.show()

print est_rows[0][:-20]