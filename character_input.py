# Ondrej Vymola 16/08/2018
# www.practicepython.org/exercise/2014/01/29/character-input.html
##################################################################
# Program asks user for name and age
# Returns the year in which you get 100 years
import string

name = "Dummy"
age = 0

name = input("Give me your name: ")
age = int(input("Thank you!\nNow give me your age: "))

result = 2018 - age + 100

count = int(input("Good job!\nHow many times would you like to see result? "))

for i in range(count):
    print(name + ", you will be 100 years old in " + str(result) +".")
