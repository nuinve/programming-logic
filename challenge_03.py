#Odd or Even Game
#Create a program that:

#Asks the user to input a number.
#If the number is even, divide it by 2.
#If the number is odd, multiply it by 3 and add 1.
#Repeat this until the number becomes 1. Print each step.

number = int(input("Enter a number: "))
result = int

if number % 2 == 0:
    result = (number/2) 
    print(f"result is: {result}")

elif number % 3 == 0: 
    result = (number*3 + 1)
    print(f"result is: {result}") 
    
    
