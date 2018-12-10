#this program counts backwards by some increment from a max_number to a min_number

max_number = 100 #set number to count backwards from
min_number = 0   #set number to count backwards to
increment  = 2   #set counting increment

i = max_number
while(i>min_number-1):
    print(i) #print counter
    i = i - 2 #count backwards
