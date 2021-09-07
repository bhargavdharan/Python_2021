# Nested loops

x = [[1,2,3],["x","y","z"]]

# for in for
for i in x:
    # print(i)
    for j in i:
        print(j, end=" ")
    print()
