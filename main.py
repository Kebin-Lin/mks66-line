from display import *
from draw import *
import math, random, colorsys

class Turtle:

    def __init__(self, x = 250, y = 250, ang = None, color = None):
        self.x = x
        self.y = y
        if (color == None):
            self.color = [int(random.random() * 256), int(random.random() * 256), int(random.random() * 256)]
        else:
            self.color = color
        if (ang == None):
            self.ang = random.random() * 2 * math.pi
        else:
            self.ang = ang
        self.penDown = False

    def fd(self, n):
        startPos = (self.x, self.y)
        self.x += n * math.cos(self.ang)
        self.y += n * math.sin(self.ang)
        if self.penDown:
            draw_line(int(startPos[0]),int(startPos[1]),int(self.x),int(self.y),screen,self.color)

    def pd(self):
        self.penDown = True

    def pu(self):
        self.pu = False

    def lt(self, ang):
        self.ang = (self.ang + ang + 2 * math.pi) % (2 * math.pi)

    def rt(self, ang):
        self.ang = (self.ang - ang + 2 * math.pi) % (2 * math.pi)

    def goto(self, x, y):
        if self.penDown:
            draw_line(int(self.x),int(self.y),int(x),int(y),screen,self.color)
        self.x = x
        self.y = y

screen = new_screen()
color = [ 0, 255, 0 ]

radius = 100
numTurtles = 64
allTurtles = []

for i in range(numTurtles):
    inAng = float(i) / numTurtles * 2 * math.pi
    hsvCol = (float(i) / numTurtles, 1, 1)
    rgbCol = colorsys.hsv_to_rgb(hsvCol[0],hsvCol[1],hsvCol[2])
    rgbCol = [int(rgbCol[0] * 255), int(rgbCol[1] * 255), int(rgbCol[2] * 255)]
    newTurt = Turtle(ang = inAng, y = 250, x = 250, color = rgbCol)
    newTurt.pd()
    allTurtles.append(newTurt)

sides = 360

for i in range(sides):
    for j in allTurtles:
        j.fd(2 * radius * math.sin(math.pi / sides))
        j.rt(1. / sides * 2 * math.pi)

numRings = 8
frequency = 8
outerTurtles = []

for i in range(numRings):
    outerTurt = Turtle(250, 250 + radius * 2.2 + i * 3, ang = 0)
    outerTurt.pd()
    outerTurtles.append(outerTurt)

for outerTurt in outerTurtles:
    dist = math.pow(math.pow(outerTurt.x - 250, 2) + math.pow(outerTurt.y - 250, 2), .5)
    start = (outerTurt.x,outerTurt.y)
    for i in range(sides):
        hsvCol = (float(i) / sides * frequency % 1, 1, 1)
        rgbCol = colorsys.hsv_to_rgb(hsvCol[0],hsvCol[1],hsvCol[2])
        rgbCol = [int(rgbCol[0] * 255), int(rgbCol[1] * 255), int(rgbCol[2] * 255)]
        outerTurt.color = rgbCol
        outerTurt.fd(2 * dist * math.sin(math.pi / sides))
        outerTurt.rt(1. / sides * 2 * math.pi)
    outerTurt.goto(start[0],start[1])

display(screen)
save_extension(screen, 'img.png')
