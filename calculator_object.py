import pyfiglet
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
                print("\033[1m" + "\033[95m" + pyfiglet.figlet_format(sum.center(65), font= "ntgreek"))
                break
            
            # if response '-', subtract the first inputted number to the second inputted number
            elif math_operator == '-':
                print("Here's for the answer:")
                resultant_value = num_1 - num_2
                difference = f"\n{num_1} - {num_2} = {resultant_value}"
                print("\033[1m" + "\033[95m" + pyfiglet.figlet_format(difference.center(65), font= "ntgreek"))
                break 
            