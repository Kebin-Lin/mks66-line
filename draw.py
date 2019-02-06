from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if x1 < x0:
        save = x1
        x1 = x0
        x0 = save
        save = y1
        y1 = y0
        y0 = save
    dy = y1 - y0
    dx = x1 - x0
    sign = dy * dx
    a = dy
    b = -1 * dx
    x = x0
    y = y0
    if (sign >= 0 and dx > dy): # 0 <= m < 1
        d = 2 * a + b
        while x < x1:
            plot(screen, color, x, y)
            if (d > 0):
                y += 1
                d += 2 * b
            x += 1
            d += 2 * a
    if (sign >= 0 and dx <= dy): # 1 <= m <= undefined
        d = a + 2 * b
        while y < y1:
            plot(screen, color, x, y)
            if (d < 0):
                x += 1
                d += 2 * a
            y += 1
            d += 2 * b
