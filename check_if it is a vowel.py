#Hola today im going to show you how to check if a letter is a vowel or not.

#First we need to create a function that will check if the letter is a vowel or not.

char = input("Enter a letter: ").lower()
if char in ('a', 'e', 'i', 'o', 'u'):
    print("It is a Vowel")

else:
    print("It is not a vowel")


