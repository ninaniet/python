import random as rnd
import matplotlib.pyplot as plt


x = [0]
y = [0]

for i in range(10000):
    los = rnd.random()
    if los == 0.01:
        x.append( (0.0 * x[i]) + (0.0 * y[i]) + (0.0))
        y.append( (0.0 *x[i]) + (0.16 * y[i]) + (0.0))


    elif los == 0.85:
        x.append((0.85 * x[i]) + (0.04 * y[i]) + (0.0))
        y.append((-0.04 * x[i]) + (0.85 * y[i]) + (1.6))
        
    elif los == 0.07:
        x.append((0.2 * x[i]) - (0.26 * y[i]) + (0.0))
        y.append((0.23 * x[i]) + (0.22 * y[i]) + (1.6))

    elif los == 0.07:
        x.append((-0.15 * x[i]) - (0.28 * y[i]) + (0.0))
        y.append((0.26 * x[i]) + (0.24 * y[i]) + (0.44))








plt.plot(x, y, '.', ms=1)
plt.show()