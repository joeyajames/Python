import turtle as tt
from random import randint, choice

def draw():
    size = randint(40, 300)
    angles = (144, 150, 157.5, 160, 165)
    angle = choice(angles)  # Using choice instead of sample for single random choice
    
    colors = [
        ('#922B21', '#E6B0AA'), ('#76448A', '#D2B4DE'), ('#1F618D', '#AED6F1'), ('#515A5A', '#EAEDED'),
        ('#148F77', '#D1F2EB'), ('#B7950B', '#F7DC6F'), ('#F39C12', '#FDEBD0'), ('#BA4A00', '#F6DDCC')]
    color = choice(colors)  # Using choice instead of sample for single random choice
    
    x_pos = randint(-200, 200)
    y_pos = randint(-200, 200)
    tt.penup()  # Correcting function name to penup
    tt.setpos(x_pos, y_pos)
    start_position = tt.pos().copy()  # Using copy to avoid modifying original position
    tt.pendown()  # Correcting function name to pendown
    
    tt.begin_fill()
    while True:
        tt.forward(size)
        tt.left(angle)
        if tt.distance(start_position) < 1:  # Using distance function for distance calculation
            break
    tt.end_fill()

tt.circle(100)
for i in range(3):
    tt.pensize(i % 3)
    draw()

tt.done()
