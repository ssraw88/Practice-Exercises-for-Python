user_input = input('Enter a number: ').split(',')
d = []
for i in user_input:
    d.append(int(i))


def formula(num):
    h = 30
    c = 50
    q = []
    for j in num:
        res = round(((2*c*j)/h)**(1/2))
        q.append(res)
    return q


result = formula(d)
print(result)
