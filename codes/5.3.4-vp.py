import matplotlib.pyplot
from numpy import arange
from numpy import meshgrid
from numpy import log

delta = 0.0025
p0range = arange(0, 1, delta)
pmrange = arange(0, 2, delta)
p0, pm = meshgrid(p0range, pmrange)

kb = 2.42

pk = []
vp = 0.01
v = 10

pth = 0.001
pp0set = [12 * pth, 10 * pth, 8 * pth, 6 * pth, 4 * pth, 2 * pth]
for pp0 in pp0set:
    gm = pm / p0
    F = vp * (gm - 1) * p0 + pth * \
        (kb * log(gm) + log(pp0 / pth)) - pp0 + pth
    kpi = vp * p0 / (v * pth)
    kpo = vp * pm / (v * pth)
    pk.append(matplotlib.pyplot.contour(kpi, kpo, F, [0]))

matplotlib.pyplot.show()
