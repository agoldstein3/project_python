#this program uses a while loop to make the robot travel in a square pattern four times

from robotsim import left, forward, right, start_simulator
start_simulator()

i = 0
while(i<4):
    i = i+1
    print(i)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
