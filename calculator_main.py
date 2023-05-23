# Ken Leam G. Gamboa
# BSCPE 1-5
# Creating an object-oriented calculator program

from user_interface import UserInterface
from calculator_object import Calculator
user_interface = UserInterface()
calculator = Calculator()

# ask for user's input
num_1 = user_interface.user_input()
num_2 = user_interface.user_input_2()
# ask for mathematical operator
math_operator = calculator.math_operator(num_1, num_2)
# create a method that can loop the program