#1️⃣ FizzBuzz Twist
#Write a program that prints numbers from 1 to 100, but:

#For multiples of 3, print "Fizz" instead of the number.
#For multiples of 5, print "Buzz".
#For numbers that are multiples of both 3 and 5, print "FizzBuzz".
#💡 Twist: Add an extra rule to replace numbers divisible by 7 with "Bang".


numbers = int

for numbers in range(1,101):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("fizzbuzz")

    elif numbers % 5 == 0:
        print("buzz")

    elif numbers  % 3 == 0:
        print("fizz")

    else:
        numbers % 7 == 0
        print("bangs")
