#this program uses the code already provided in the chapter 2 exercise, and uses a "scale" value to change the size of the smiley face

from cs1lib import start_graphics, clear, draw_circle, draw_rectangle, set_fill_color, set_stroke_color

def draw():

    x = 200 #change x location of the center of the circle
    y = 200 #change y location of the center of the circle
    scale = 3 #scale the size of the smiley face


    # draw a white background
    clear()

    # draw the outline of the face
    set_fill_color(1, 1, 0)   # set fill color to yellow
    draw_circle(x, y, 50*scale)

    # draw the mouth
    set_fill_color(1, 1, 0)  # yellow
    draw_circle(x, y, 30*scale)
    set_stroke_color(1, 1, 0)
    draw_rectangle(x - 32*scale, y - 32*scale, 62*scale, 40*scale)

    # draw the eyes
    set_stroke_color(0, 0, 0)
    set_fill_color(0, 0, 0)  # set fill color to black
    draw_circle(x - 20*scale, y - 10*scale, 5*scale)
    draw_circle(x + 20*scale, y - 10*scale, 5*scale)

start_graphics(draw)
