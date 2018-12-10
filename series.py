#this program calculates and prints the first 100 numbers in a series defined by the difference of two consecutive numbers increasing by one for each new number
count = 1
diff = 1

while diff <= 100:
    print(count)
    count = count + diff
    diff = diff + 1
