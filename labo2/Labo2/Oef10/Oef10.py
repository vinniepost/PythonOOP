

for x in range(1,100,1):
    if (x%3 == 0 | x%5==0):
        print("FizzBuzz");
    elif (x%5==0):
        print("Buzz");
    elif (x%3==0):
        print("Fizz");
    print(x)