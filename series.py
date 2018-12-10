#this program calculates and prints the first 100 numbers in a series defined by the difference of two consecutive numbers increasing by one for each new number
count = 1 #initialize first number in series
diff = 1 #initialize difference between two numbers in series

while diff <= 100:
    print(count)
    count = count + diff
    diff = diff + 1
