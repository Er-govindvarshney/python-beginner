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

# #White a program to check if a number is positive negative or zero.
print("Enter any number n")
n = int(input("enter n = "))
if( n > 0 ):
    print("positive")
elif( n < 0 ):
    print("negative")
elif( n == 0 ):
    print("zero")
else:
    print("Not defined")

#Write a program to check the type of triange.
print("Enter sides of triangle a b and c")
a = int(input("enter a = "))
b = int(input("enter b = "))
c = int(input("enter c = "))
if ( a == b and b == c and c == a ):
    print("Trianbgle is equilateral")
elif( a == b and c != a and c != b):
    print("Triange is isosceles")
elif( a != b and b != c and c != a):
    print("triangle is scelen")
else:
    print("Not defined")

# Write a program to calculate electricity bill where 5 rupees for first 100 then 7 rupees for more than 100 to 200 then10 for next 100 units.
print("Enter number is unit u")
u = int(input("enter n = "))
if( u <= 100 ):
    print(u*5)
elif( 200 >= u >= 101):
    print((100*5)+(u-100)*7)
elif( 201 <= u ):
    print((100*5)+(100*7)+(u-200)*10)
else:
    print("bill is zero")




