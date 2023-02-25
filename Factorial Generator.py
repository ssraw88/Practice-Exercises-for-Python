# Using factorial function from the math library
from math import factorial
user_input = int(input('Enter the number: '))

factorial_of_user_input = factorial(user_input)  # This will store the factorial

print(factorial_of_user_input)

# Using 'while' loop for the same.
user_input = user_input + 1  # To make the range of 'while' and 'for' loop easier
i = 1  # This will be used to iterate upon
total = 1  # This will contain the value of factorial

while i < user_input:
    total = total * i  # The value will increase every time the condition is iterated upon
    i += 1

print(total)

# Using 'for' loop
temp = 1
for j in range(1, user_input):
    temp *= j

print(temp)
