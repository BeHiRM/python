import color

def shine(c):
    red = c.getRed()
    green = c.getGreen()
    blue = c.getBlue()
    return (.299 * red) + (.587 * green) + (.114 * blue)
