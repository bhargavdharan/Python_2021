marks = int(input("Enter the marks:"))
print(marks)

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "E"

print(f"The marks of the student is {marks} and grade is {grade}")


a1 = input("Enter the value:")
print(a1, type(a1))
if a1 == "pointbreaker":
    print("welcome Thor")
else:
    print("wrong password")

