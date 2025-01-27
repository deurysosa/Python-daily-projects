#Program to check if a number is even or odd
#Author: PyDeu

#Here we take an input from the user and check if the number is even or odd
number = int(input("Enter a number you want to check: "))

#We use the modulo operator to check if the number is divisible by 2 or not. 
#If it is divisible by 2 then it is even else it is odd. 
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd") 

#Thas it!