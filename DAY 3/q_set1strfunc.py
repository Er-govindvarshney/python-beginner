#WAP to input user’s first name & print its length. 
print("Enter your first name")
name = str(input("please tell us your name : "))
str1 = len(name)
print(str1 , "is the length of your name")

#WAP to find the occurrence of ‘$’ in a String.
print("Enter your string")
string = str(input("Write here : "))
count = string.count("$")
print(count)

#WAP to check if any string ends with "an".
print("Enter your string")
string = str(input("Write here : "))
str1 = string.endswith("an")
print(str1)

#WAP to capitalize the first letter of string entered by user.
print("Enter your string")
string = str(input("Write here : "))
str1 = string.capitalize()
print(str1)

#Take sentence as input and count how many times "the" appears.
print("Please enter your sentence")
sen = str(input("sentence : "))
sen1 = sen.count("the")
print(sen1)

#Replace all the spaces with "_" in " I love programming . "
str = " I love programming . "
str1 = str.replace(" " , "_")
print(str1)