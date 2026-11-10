#Write a program for the gievn marking system.
#Grade students based on marks
#marks >= 90, grade = "A"
#90 > marks >= 80, grade = “B”
#80 > marks >= 70, grade =“C”
#70 > marks, grade = "D"

print("ENTER YOUR MARKS")
m = int(input("enter marks = "))
if(100 >= m >= 90):
    print("A")
elif(90 > m >= 80):
    print("B")
elif(80 > m >= 70):
    print("C")
elif(70 > m):
    print("D")
else:
    print("NOT DEFINED")
print("ALL THE BEST FOR YOUR FUTURE USER")

# WAP to check if a number entered by the user is odd or even.
print("ENTER YOUR NUMBER n")
n = int(input("enter n = "))
if( n%2  == 0):
    print("Even")
else:
    print("Odd")

# WAP to find the greatest of 3 numbers entered by the user.
print("Enter number a b and c")
a = int(input("enter a = "))
b = int(input("enter b = "))
c = int(input("enter c = "))
if(a >= b  and  a >= c):
    print("a is greater " , a)
elif(b >= a  and  b >= c):
    print("b is greater " , b)
else:
    print("c is greater " , c)

# WAP to check if a number is a multiple of 7 or not.
print("ENTER NUMBER n")
n = int(input("enter n = "))
if(n%7 == 0):
    print(n , " is multiple of 7")
else:
    print("Not a multiple")


