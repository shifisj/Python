LIMIT = 101
for n in range(1,LIMIT):
    if n % 3 == 0 and n % 5 == 0:
        print ("FIZZBUZZ")
    elif n % 3 == 0:
        print ("FIZZ")
    elif n % 5 ==0:
        print ("BUZZ")
    else:
        print(n)