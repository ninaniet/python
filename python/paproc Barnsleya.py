import random as rnd
import matplotlib.pyplot as plt


x = [0]
y = [0]

for i in range(10000):
    los = rnd.random()
    if los < 0.5:
        x.append( (0.0 * x) + (0.0 * y) + (0.0))
        y.append( (0.0 *x) + (0.16 * y) + (0.0))


    else:
        x.append((0.85 * x) + (0.04 * y) + (0.0))
        y.append((-0.04 * x) + (0.85 * y) + (1.6))