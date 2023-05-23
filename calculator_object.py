# create a class named 'Calculator'
class Calculator:
# create a method to determine what mathematical operator will be used

    def math_operator(self):
        while True:
            # ask user for what operator to use
            print("\033[95m" + "\nInput one of the following values to determine what mathematical operator will be used for calculation.\n")
            print("Use '+' to indicate addition\nUse '-' to indicate subtraction\
                \nUse 'x' to indicate multiplication\nUse'/' to indicate division")
            math_operator = str(input("\nInput what operator to use: "))
            math_operator = math_operator.lower()
            return math_operator
