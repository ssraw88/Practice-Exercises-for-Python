user_input = int(input('Enter a number: '))

dictionary_for_squares = {}

for i in range(1, user_input+1):
    dictionary_for_squares[i] = i*i

print(dictionary_for_squares)
