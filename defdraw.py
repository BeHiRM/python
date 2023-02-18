import math
import stddraw
import sys

n = int(sys.argv[1])
x, y = [], []

for i in range(n + 1):
    x += [math.pi * i / n]
    y += [math.sin(4*x[i]) + math.sin(20*x[i])]

stddraw.setXscale(0, math.pi)
stddraw.setYscale(-2.0, 2.0)

for i in range(n):
    stddraw.line(x[i], y[i], x[i+1], y[i+1])
stddraw.show()
