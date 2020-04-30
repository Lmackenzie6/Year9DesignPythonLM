#Comments are made with a #
#It is essential you comment your code

#This program will take two integers
#and multiply them

#Input
#The input function returns the string the user enters
#All inputs start as strings
#To change the type of variables you "cast" it
#Casting is the process of changing type
name = input("Please input your name: ")
a = input("Please input first number: ")
a = int(a) #self-referencing assignment statement
b = input("Please input second number: ")
b = int(b)

#Process
#What is process
product = a * b



#Output
print("Hi, "+name)
print("The product of "+str(a)+" and "+str(b)+" is "+str(product)+",")