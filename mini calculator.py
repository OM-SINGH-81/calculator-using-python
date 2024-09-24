a=int(input("Enter first Number"))
b=int(input("Enter second Number"))

print("select + sum of two no.")
print("select - subtract of two no.")
print("select / division of two no.")
print("select * multiplication of two no.")

choice=input("Enter Choice")

if (choice=="+"):
    print("Sum of two no.= ",a+b)
elif (choice=="-"):
    print("Subtract of two no.= ",a-b)
elif (choice=="/"):
    if (n2!=0):
         print("Division of two no.= ",a/b)
    else:
         print("not divisible")
elif (choice=="*"):
    print("Multiplication two no.= ",a*b)
else:
    print("invalid choice")
