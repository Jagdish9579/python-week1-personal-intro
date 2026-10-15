# Week 1 Project: Personal Introduction Program
# This program asks the user questions and displays a welcome message.

print("===================================")
print("   PERSONAL INTRODUCTION PROGRAM")
print("===================================")

# Get information from the user
name = input("What is your name? ")
age = input("How old are you? ")
hobby = input("What is your favorite hobby? ")

# Ask additional questions
city = input("Which city do you live in? ")
favorite_food = input("What is your favorite food? ")

# Display a personalized welcome message
print("\n===================================")
print(f"🎉 Welcome, {name}! 🎉")
print("===================================")

print(f"You are {age} years old.")
print(f"You live in {city}.")
print(f"Your favorite hobby is {hobby}.")
print(f"Your favorite food is {favorite_food}.")
print("\nThank you for introducing yourself!")
print("Happy learning Python! 🚀")