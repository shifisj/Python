def fizzbuzzfn (n:int):
    if n % 3 == 0 and n % 5 == 0:
        return "FIZZBUZZ"
    if n % 3 == 0:
        return "FIZZ"
    if n % 5 ==0:
        return "BUZZ"
    return n 
LIMIT = 101
for n in range(1,LIMIT):
    print(fizzbuzzfn(n)) 