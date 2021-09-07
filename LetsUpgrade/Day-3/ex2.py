# call by value or call by reference

# def fun1(list1):
#     print ("List1 before append :",list1)
#     list1.append(68)
#     print ("list1 after append :",list1)

# list1=[10,20]
# fun1(list1)
# print("Outside \t:",list1)

#--------------------------------------------------

# def fun1(a):
#     print("before a: \t",a)
#     print("Address before: \t",id(a))
#     a = a+10
#     print("After a: \t",a)
#     print("Address After: \t",id(a))

# a = 200
# fun1(a)

# print("After calling: ",a)
# print("After calling value address: ",id(a))
# # print("After calling: ",fun1(a))

#-------------------------------------------------

# k = 100
# def fun1():
#     global k
#     k = k + 100
#     print(k)

# fun1()
# print("After: \t",k)

#-------------------------------------------------

def fun1(a, list1=[]):
    list1.append(a)
    print(list1)

fun1(10)
fun1(20)
fun1(20,[])
fun1(20,[10,20,30])
fun1(30)










