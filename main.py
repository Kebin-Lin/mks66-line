from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

for i in range(10):
    draw_line(250, 250, int((i / 10) * 10),

display(screen)
save_extension(screen, 'img.png')
