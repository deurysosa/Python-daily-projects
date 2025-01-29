#Hello here im going to write a program that will check if a string is a palindrome or not

#A palindrome is a word that reads the same forwards and backwards
#For example: "racecar" is a palindrome
#so the first thing we need to do is to ask the user to enter a word

word = input("Enter a word: ")

#Now we need to check if the word is a palindrome
#To do this we can use the slicing method   word[::-1]
#This method will reverse the word

if word == word[::-1]:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")

#Now the proram is done.