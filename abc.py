c=1000 #global

def f1():
 
    a=100 #local
    b=200 #local

    print(c)

def f2():
    print(c)


f1()
f2()
