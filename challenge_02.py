#Palindrome Checker
#Create a function that takes a string and returns True if it’s a palindrome (it reads the same backward as forward), ignoring spaces and punctuation.
#💡 Hint: Use string slicing and str.lower() to make the check case-insensitive.

word = input("Enter a word: ").lower()

def palindrome():

    if word == word[::-1]:
        print("it's a palindrome")
    else:
        print("it's not a palindrome")
        
palindrome()

#remembering: in python, def's name need to bee different from the variable