import turtle as tt
from random import choice, randint

def draw():
    max_size = min(tt.window_height(), tt.window_width()) / 2 - 50
    size = randint(40, int(max_size))
    angles = (144, 150, 157.5, 160, 165)
    angle = choice(angles)
    
    colors = [
        ('#922B21', '#E6B0AA'), ('#76448A', '#D2B4DE'), ('#1F618D', '#AED6F1'), ('#515A5A', '#EAEDED'),
        ('#148F77', '#D1F2EB'), ('#B7950B', '#F7DC6F'), ('#F39C12', '#FDEBD0'), ('#BA4A00', '#F6DDCC')]
    color = choice(colors)
    tt.color(color[0], color[1])
    
    x_pos = randint(-int(max_size), int(max_size))
    y_pos = randint(-int(max_size), int(max_size))
    tt.pu()
    tt.setpos(x_pos, y_pos)
    start_position = tt.pos()
    tt.pd()
    
    tt.begin_fill()
    while True:
        tt.forward(size)
        tt.left(angle)
        if tt.distance(start_position) < 1:
            break
    tt.end_fill()
    
tt.circle(100)
for i in range(3):
    tt.pensize(i % 3)
    draw()

tt.mainloop()
