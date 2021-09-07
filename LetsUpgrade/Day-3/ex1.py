# def fun1(a,b=0):
#     c = a + b
#     # print("Inside a", id(a))
#     print(c)
#     return c

# # x = 100
# # y = 200
# # # print("outside",id(x))

# # d = 400

# # d = d + (fun1(x,y))
# # fun1(d)

# print(fun1(10,20))
# print(fun1(20))

#---------------------------------------------------

# def fun1(name,age=18,marks=50):
#     # print(f"Name:{name}\t Age:{age}\t Marks:{marks}")
#     print(f"{name}\t {age}\t {marks}\t")

# print("Name\t Age\t Marks\t")
# fun1("Manish",21,89)
# fun1("Bhaskar",23,90)
# fun1("Arjun",28,90)

#---------------------------------------------------

# def fun1(a,*b):
#     print(a,"\t",b)


# fun1(10,20)
# fun1(30)
# fun1(8,9,4,5,6,7,8)

#----------------------------------------------------

# def fun1(**kwargs):  # kwargs = key worded arguments
#     print(kwargs)


# fun1(brand="intel",gene="11th",pro="i7")

#-----------------------------------------------------

# ()
def fun1(a,b=0,*args,**kwargs):
    print(a,b,args,kwargs)

fun1(1,2,34,56)

# when the interpreter define b=0?
# ans -- At the definition

#--------------------------------------------------------

