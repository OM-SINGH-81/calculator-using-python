a=int(input("Enter starting ponit = "))
b=int(input("Enter ending ponit = "))
c=int(input("Enter updation choice = "))

print("Choice 'h' for horizantol")
print("Choise 'v' for vertical")

d=input("Enter your choice = ")

if (d=="h"):
    print("Choice 'f' for forward order")
    print("choice 'r' for reverse order")

    r=input("Enter your choice = ")

    if (e=="f"):
        for i in range(a,(b+1),c):
            print(i,end=' ')

    elif (e=="r"):
        for i in range(b,(a-1),-c):
            print(i,end=' ')

    else:
        print("Invalid Choice")

elif (d=="v"):
    print("Choice 'f' for forward ")
    print("choice 'r' for reverse ")
    e=input("Enter your choice = ")

    if (e=="f"):
        for i in range(a,(b+1),c):
            print(i)

    elif (e=="r"):
        for i in range(b,(a-1),-c):
            print(i)

    else:
        print("Invalid Choice")


else:
    print("Invalid choice")