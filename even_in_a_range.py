#this program tests whether a number 1) falls in the range [24,32]; and 2) is even.

x = 33 # number to test
print((x<33 and x>23) and x % 2 == 0) #set conditions; first condition gives range, second checks if round-off equals zero. 
                                      #if round-off equals zero, the value is even.
