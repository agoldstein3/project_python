#this program is intended to define a function that takes in a scaling parameter to make a robot move in a square of size s.

from robotsim import *

start_simulator()

def square_scale(s):
    forward(50*s)                  # go straight a few feet
    left(90)                      # turn left 90 degrees
    forward(50*s)                  # go straight a few feet
    left(90)                      # turn left 90 degrees
    forward(50*s)                  # go straight a few feet
    left(90)                      # turn left 90 degrees
    forward(50*s)                  # go straight a few feet
    left(90)                      # turn left 90 degrees
    
s = 2 # define scaling parameter
square_scale(s) #call to function and pass scaling parameter
