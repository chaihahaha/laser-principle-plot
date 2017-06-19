import matplotlib.pyplot
from numpy import arange
from numpy import meshgrid
from numpy import log

delta = 0.025
krange = arange(0, 20.0, delta)
grange = arange(0, 8.0, delta)
k, g = meshgrid(krange, grange)
lset = [2.6666666666666665, 2.3333333333333335, 2.0, 1.6666666666666667,
        1.3333333333333333, 1.0, 0.6666666666666666, 0.3333333333333333]
r = 1.1
b = 3
b0 = 1
kg = []
for l in lset:
    F = log(k * r - r * l * b / (r + 1) - log(g) * b * r / (b0 * (r + 1))
            ) + l * b / (r + 1) - r * b * log(g) / (b0 * (r + 1)) - log(k * r)
    H = 0
    kg.append(matplotlib.pyplot.contour(k, g, (F - H), [0]))

matplotlib.pyplot.show()
