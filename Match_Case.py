import sys

d=list(sys.version_info)

if d[1]==11:
    op={1:'+',2:'-',3:'*',4:'/'}
    n1=eval(input("Enter first number : "))
    n2=eval(input("Enter second number : "))
    o=eval(input(f"Enter operator\n{list(op.keys())}\n{list(op.values())} :"))
    val=op.get(o)
    match val:
        case '+':
            print(f"{n1}+{n2}={n1+n2}")
        case '-':
            print(f"{n1}-{n2}={n1-n2}")
        case '*':
            print(f"{n1}*{n2}={n1*n2}")
        case '/':
            print(f"{n1}/{n2}={n1/n2}")
        case _:
            print("Please choice correct operator !")

else:
    print("Please download latest python version otherwise you could not execute Match case statement ")
