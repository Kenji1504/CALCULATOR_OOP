# Ken Leam G. Gamboa
# BSCPE 1-5
# Creating an object-oriented calculator program

from user_interface import UserInterface
from calculator_object import Calculator
calculator = Calculator()
user_interface = UserInterface()
# call out program title method
user_interface.program_title() 
# call out the loop method
calculator.loop_calculator()