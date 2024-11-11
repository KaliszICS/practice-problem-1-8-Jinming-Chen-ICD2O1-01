'''
    Lesson: Boolean Logic
    Author:Jinming Chen     
    Date Created: Sept 26, 2024
    Date Last Modified: Sept 26, 2024
'''
def q1():
  #Write Assignment code here
  # Create a Boolean value
bool1 = True
bool2 = False

# OR operation result
print(bool1 or bool2)
print(bool2 or bool1)

def q2():
  #Write Assignment code here
# Ask the user to enter an integer
num = input("Enter an integer: ")
# Check if the integer is 0 and print the result
print(num != 0)
def q3():
  #Write Assignment code here
# Ask the user to enter a number
num = float(input("Enter a number: "))
# Check if the number is between 0 and 10 and print the result
print(0 <= number <= 10)
def q4():
  #Write Assignment code here
# Ask the user to input food and drink
food = input("Input food: ")
drink = input("Input drink: ")
# Check if the input is pizza and pop
print(not (food == "pizza" and drink == "pop"))
def q5():
  #Write Assignment code here

#Do not edit code after this
#Comment out the followwing code when running tests

q1()
q2()
q3()
q4()
q5()
