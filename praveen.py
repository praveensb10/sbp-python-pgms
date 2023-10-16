a=int(input("enter first:"))
b=int(input("enter second:"))

for i in range(a,b):
    if i%2==0:
        print(i, "is even")
    else:
        print(i, "is odd")