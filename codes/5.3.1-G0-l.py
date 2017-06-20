import matplotlib.pyplot
from numpy import arange
from numpy import meshgrid
from numpy import log

delta = 0.025
lrange = arange(0, 10.0, delta)
grange = arange(0, 30.0, delta)
l, g = meshgrid(lrange, grange)
kset = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
r = 1.1
b = 2
lb = l * b
b0 = 1
lg = []
for k in kset:
    F = log(k * r - r * l * b / (r + 1) - log(g) * b * r / (b0 * (r + 1))
            ) + l * b / (r + 1) - r * b * log(g) / (b0 * (r + 1)) - log(k * r)
    H = 0
    lg.append(matplotlib.pyplot.contour(lb, g, (F - H), [0]))

matplotlib.pyplot.show()
