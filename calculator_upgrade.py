# Ken Leam G. Gamboa
# BSCPE 1-5
# Inheriting the Calculator class, and adding other methods such as: Square of a number,
# Exponentiation, Square root, and Pythagorean Theorem 

import time
from calculator_object import Calculator


class UpgradedCalculator(Calculator):
    # create a method that squares a number
    def square(self, num_1, num_2):
        print("Here's for the answer:")
        time.sleep(1)
        resultant_value1 = num_1 ** 2
        resultant_value2 = num_2 ** 2            
        answer_1 = f"\n ({num_1})² = {resultant_value1}"
        answer_2 = f"\n ({num_2})² = {resultant_value2}"
        print("\033[1m" + "\033[95m" + answer_1.center(100))
        time.sleep(1)
        print("\033[1m" + "\033[95m" + answer_2.center(100))
    
    # create a method that multiplies the number based on its exponents
    def exponent(self, num_1, num_2):
        time.sleep(1)
        resultant_value = num_1 ** num_2
        answer = f"\n ({num_1})^{num_2} = {resultant_value}"
        print("\033[1m" + "\033[95m" + answer.center(100))
        time.sleep(1)
    # create a method that solves for the square root of a number
