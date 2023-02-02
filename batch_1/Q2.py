import sys

# find non Prime


def isNotPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return True
    return False


def rangeNonPrime(start, end):
    for i in range(start, end+1):
        if isNotPrime(i):
            print(i)

a=[]
def fibnoccai(n):
    if n == 1:
        a.append(0)
        return a
    elif n == 2:
        a.append(1)
        return a
    else:
        a.append(fibnoccai(n-1)+fibnoccai(n-2))
        return a


if __name__ == '__main__':
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    # rangeNonPrime(start,end)
    print(fibnoccai(end))
