a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))
if(a >=b and a >= c and a >= d):
    print("a is the largest number")
elif(b >= c and b >= d):
    print("b is the largest number")
elif(c >= d):
    print("c is the largest number")
else:
    print("d is the largest number")
