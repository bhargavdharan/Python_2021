val = int(input("Enter the multiple of 7:"))
while val%7 !=0:
    val = int(input("Enter the multiple of 7:"))
else:
    print("%d this number is multiple of 7" %val)