#Write a loop that simulates flipping a coin 5 times, and prints out “heads” or “tails” after each flip. Use the Python
#randint function to determine if the outcome of each flip should be heads or tails.

from random import randint

n = 1 #lower random number bound
m = 100 #upper random number bound

i = 0 #initialize loop
max = 5 #number of times you want to flip the coin

while(i<max):
    i = i+1
    #print("you are on iteration", i) #check where you are in the loop
    x = randint(n,m)
    #print("your random number is", x) #display random number
    
    #if the random number is even (odd), display heads (tails)
    if x % 2 == 0:
        print("heads")
    else:
        print("tails")
