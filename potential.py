import stddraw
import stdio
import stdarray
from charge import Charge
from color import Color
from picture import Picture

# Read values from standard input to create an array of charged
# particles. Set each pixel color in an image to a grayscale value
# proportional to the total of the potentials due to the particles at
# corresponding points. Draw the resulting image to standard draw.

MAX_GRAY_SCALE = 255

# Read charges from standard input into an array.
n = stdio.readInt()
charges = stdarray.create1D(n)
for i in range(n):
    x0 = stdio.readFloat()
    y0 = stdio.readFloat()
    q0 = stdio.readFloat()
    charges[i] = Charge(x0, y0, q0)