#Write a function that takes a list and returns it reversed, without using the reverse() method.

x = list(input("Enter a list: "))
y = []

def reverse_list(x):
    for i in range(len(x)-1, -1, -1): #remembering: iteration, index, element (3 arguments)
        y.append(x[i])
    return y

result = reverse_list(x)
print(f"reverse mode: {result}")


