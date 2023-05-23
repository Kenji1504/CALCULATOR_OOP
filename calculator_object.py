# create a class named 'Calculator'
class Calculator:
# create a method to determine what mathematical operator will be used

    def math_operator(self, num_1, num_2):
        while True:
            # ask user for what operator to use
            print("\033[95m" + "\nInput one of the following values to determine what mathematical operator will be used for calculation.\n")
            print("Use '+' to indicate addition\nUse '-' to indicate subtraction\
                \nUse 'x' to indicate multiplication\nUse'/' to indicate division")
            math_operator = str(input("\nInput what operator to use: "))
            math_operator = math_operator.lower()
            
            # if response is '+', add two values
            if math_operator == '+':
                print("Here's for the answer:")
                resultant_value = num_1 + num_2
                sum = f"\n{num_1} + {num_2} = {resultant_value}"
                print(sum)
                break

            