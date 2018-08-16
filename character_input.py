# Ondrej Vymola 16/08/2018
# www.practicepython.org/exercise/2014/01/29/character-input.html
##################################################################
# Program asks user for name and age
# Returns the year in which you get 100 years

name = "Dummy"
age = 0

name = str(input("Give me your name: "))
age = int(input("Thank you!\nNow give me your age: "))

result = 2018 - age + 100

print(name + ", you will be 100 years old in " + str(result) +".")
