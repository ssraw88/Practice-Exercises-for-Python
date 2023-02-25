user_input1 = int(input('Enter first number: '))  # User will enter the first number for the range.
user_input2 = int(input('Enter second number: '))  # User will enter the last number for the range.
user_input2 = user_input2 + 1  # This is done so that the range() function checks the last number input by the user.
list_of_divisible = []  # An empty list to insert all the numbers divisible by 7 but not by 5.

for i in range(user_input1, user_input2):
    if i % 7 == 0 and i % 5 != 0:
        list_of_divisible.append(i)  # Every number which returns true will be appended to the list.

print(list_of_divisible)
