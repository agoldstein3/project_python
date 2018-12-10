#Write a function that draws a smiley face. The function should take three parameters that
#indicate the location and size of the smiley face. Call the function to draw a smiley face with
#radius of 25 centered at 100, 150 on the screen. The size should be specified in pixels; you will
#need to compute and make use of a scaling factor based on that size.

from cs1lib import start_graphics, clear, draw_circle, draw_rectangle, set_fill_color, set_stroke_color

x = 100
y = 150
scale = 0.5

def draw(x,y,scale):

    #x = 100
    #y = 150

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

def draw_smiley():
    clear()
    draw(x, y, scale)
    
start_graphics(draw_smiley)
