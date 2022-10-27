print("Enter which program you wish to run")
print("1 for simple inheritance")
print("2 for Multiple Inheritance")
print("3 for multilevel Inheritance")
type_of_inheritance=int(input())
if(type_of_inheritance==1):
    print("You have chosen Single Inheritance")
    class Parent:
        __x=9
        y=9
        def func1(self):
            print("this is function one")


    class Child(Parent):
        #x = 10
        def func2(self):
            print("This is function 2 ")
    ob = Child()
    print(ob.x)
    print(ob.y)
    ob.func1()
    ob.func2()
elif(type_of_inheritance==2):
    print("You have chosen Multiple Inheritance")

    class Parent:
        def func1(self):
            print("this is function 1")
    class Parent2:
        x=9
        def func2(self):
            print("this is function 2")
    class Child(Parent, Parent2):
        def func3(self):
            print("this is function 3")

    ob = Child()
    print(ob.x)
    ob.func1()
    ob.func2()
    ob.func3()
elif(type_of_inheritance==3):
    print("You have chosen Multilevel Inheritance")


    class Parent:
        x = 9
        def func1(self):
            print("this is function 1")


    class Child(Parent):
        def func2(self):
            print("this is function 2")


    class Child2(Child):
        def func3(self):
            print("this is function 3")


    ob = Child2()
    ob1=Child()
   # ob1.func3()
    print(ob.x)
    ob.func1()
    ob.func2()
    ob.func3()
else:
    print("Please enter the value as 1,2 or 3 only")