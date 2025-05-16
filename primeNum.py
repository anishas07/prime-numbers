from math import sqrt
Number = int(input("Enter a number"))
if Number > 1:
    for k in range(2, int(sqrt(Number))+1):
        if (Number % k) ==0:
            print(Number, "This is not a prime number")
            break
        else:
            print(Number,"This is a prime number")