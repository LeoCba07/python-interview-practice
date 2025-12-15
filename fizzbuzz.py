def fizzbuzz(n):
    for num in range(1, n + 1):
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)

fizzbuzz(15)

# If divisible by 3 → print "Fizz"
# If divisible by 5 → print "Buzz"
# If divisible by both → print "FizzBuzz"
