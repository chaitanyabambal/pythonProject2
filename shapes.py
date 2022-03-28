def rectangle(a, b):
    return a*b
def perimeter(a, b):
       return a+a+b+b
def square(a):
    return  a*a



if __name__=="__main__":

print("Menu\n 1.Area of Rectangle\n 2.Perimeter of Reactangle\n 3.Area of Square")
x = int(input("Please Enter your Choice Given:\n"))
if x==1:
    a1 = int(input("Enter value1"))
    a2 = int(input("Enter value2"))
    print( rectangle(a1,a2))
elif x==2:
    a1 = int(input("Enter value1"))
    a2 = int(input("Enter value2"))
    print(perimeter(a1, a2))

elif x==3:
    a1 = int(input("Enter value1"))
    a2 = int(input("Enter value2"))
    print(square(a1))
else:
    print("Its the wrong input")

