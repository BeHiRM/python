
import stddraw
RADIUS, DT = 0.04, 08.0
stddraw.setXscale(-1.0, +1.0)
stddraw.setYscale(-1.0, +1.0)

rx, ry = .480, .860
vx, vy = .015, .023

while True:
    if abs(rx + vx) + RADIUS > 1.0:
        vx = -vx
    if abs(ry + vy) + RADIUS > 1.0:
        vy = -vy
    rx += vx
    ry += vy
    stddraw.clear(stddraw.GRAY)
    stddraw.filledCircle(rx, ry, RADIUS)
    stddraw.show(DT)
