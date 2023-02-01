a = [i for i in range(1, 11)]


def check(x):
    if (x % 2 == 0):
        return True
    return False


result = filter(check, a)  # using filter

for i in result:
    print(i)


    
# print(result)
# print(type(result))
