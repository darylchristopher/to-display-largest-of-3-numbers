n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the thrid number: "))
if(n1>=n2)and(n1>=n3):
    biggest=n1
elif(n2>=n1)and(n2>=n3):
    biggest=n2
else:
    biggest=n3
print("The largest number is ",biggest)
