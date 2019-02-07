from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(250,0,250,500,screen,color)
draw_line(0,250,500,250,screen,color)
draw_line(0,0,500,500,screen,color)
draw_line(0,500,500,10,screen,color)

for i in range(-15,16):
    draw_line(250, 250, 300, i * 10 + 250, screen, color)

display(screen)
save_extension(screen, 'img.png')
