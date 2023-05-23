import pyfiglet
from user_interface import UserInterface
user_interface = UserInterface()
# create a class named 'Calculator'
class Calculator:
# create a method to determine what mathematical operator will be used
# (the output will be also printed when this method is called out)
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

            # if response is 'x', multiply the first inputted number to the second inputted number
            elif math_operator == 'x':
                print("Here's for the answer:")
                resultant_value = num_1 * num_2
                product = f"\n{num_1} x {num_2} = {resultant_value}"
                print("\033[1m" + "\033[95m" + pyfiglet.figlet_format(product.center(65), font= "ogre"))
                break

             # if response is '/' 
            elif math_operator == '/':
                # inside while loop
                while True:
                    # try dividing the first inputted number to the second inputted number
                    try:
                        resultant_value = num_1 / num_2
                        quotient = f"\n{num_1} / {num_2} = {resultant_value}"
                        print("Here's for the answer:")
                        print("\033[1m" + "\033[95m" + pyfiglet.figlet_format(quotient.center(65), font= "ogre"))
                        break
                    # use except function to capture any Zero Division Error
                    except ZeroDivisionError:
                        print("\033[31m" + "\nInvalid Input. You're trying to divide a particular number by 0\n")
                        print("\033[95m" + "Please try again.")
                    # break the loop
                    break
                break
            # else, print Invalid Input
            else:
                print("\033[31m" + "INVALID INPUT, please try again")

# create a method that can loop the program
    def loop_calculator(self):
        # To loop the program, create a while loop
        while True:
            # call out the calculator function
            num_1 = user_interface.user_input()
            num_2 = user_interface.user_input()
            self.math_operator(num_1, num_2)
            # ask user if they want to try again
            while True:
                repeat_program = str(input("\033[95m" + "\nDo you want to try again? (y/n): "))
                repeat_program = repeat_program.lower()
                # if response is 'yes', continue
                if repeat_program == "y":
                    break
                # if response in 'no', break
                elif repeat_program == "n":
                    # end program
                    END_PROGRAM = "END"
                    print ("\n" + "\033[1m" + END_PROGRAM.center(90, "-"))
                    exit()
                else:
                    # print 'Invalid Input'
                    print("\n\033[31m" + "INVALID INPUT, please try again.")
