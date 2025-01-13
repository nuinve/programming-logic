#Given a list of numbers, write a function to find the second largest number.

numbers = list(map(int, input("Enter a list of numbers: " ).split()))

def largest_number(numbers):
    x = list(set(numbers))
    x.sort(reverse=True)
    return x[1]

largest = largest_number(numbers)
print(f"the 2nd largest nsumber is: {largest}")


