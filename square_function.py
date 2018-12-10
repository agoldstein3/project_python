#Objective: Use a function to isolate a sequence of instructions, encapsulating a complex behavior. This is an example of abstraction.

#Write a function single_square() that causes the robot to do a single square. 
#Also write a while loop that calls single_square() 5 times, to cause the robot to drive in 5 squares.

from robotsim import left, forward, right, start_simulator
start_simulator()

#create function to make the robot move in a square pattern
def single_square():
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    
#create while loop to make the robot move in the square pattern five times
i = 1 #initialize loop
while(i<6):
    i = i+1
    #print(i)
    single_square()
