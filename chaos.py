import sys
import random
import stddraw
from stddraw import RED, GREEN, BLUE
n = int(input())
cx = [0.0, 1.0, 0.500]
cy = [0.0, 0.0, 0.866]
colores = [RED, GREEN, BLUE]
x, y = 0, 0
for i in range(n):
    r = random.randrange(0, 3)
    x = (x + cx[r]) / 2.0
    y = (y + cy[r]) / 2.0
    stddraw.setPenColor(colores[r])
    stddraw.point(x, y)
    stddraw.show(0)

stddraw.show()
