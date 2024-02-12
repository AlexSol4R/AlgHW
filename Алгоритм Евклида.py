def NOD1(x,y):
    while x!=0:
        if y>x:
            x,y=y,x
        x=x%y
        print(x,y)
    return y

def NOD2(x,y):
    while x!=y:
        if y>x:
            x,y=y,x
        x-=y
        print(x,y)
    return x

a=int(input("a = "))
b=int(input("b = "))

print("НОД 1 способ:", NOD1(a,b))
print("НОД 2 способ:", NOD2(a,b))