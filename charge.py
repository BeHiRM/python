import sys
import math
import stdio

#-----------------------------------------------------------------------

class Charge:

    # Construct self centered at (x, y) with charge q.
    def __init__(self, x0, y0, q0):
        self._rx = x0  # x value of the query point
        self._ry = y0  # y value of the query point
        self._q = q0   # Charge

    # Return the potential of self at (x, y).
    def potentialAt(self, x, y):
        COULOMB = 8.99e09
        dx = x - self._rx
        dy = y - self._ry
        r = math.sqrt(dx*dx + dy*dy)
        if r == 0.0: # Avoid division by 0
            if self._q >= 0.0:
                return float('inf')
            else:
                return float('-inf')
        return COULOMB * self._q / r