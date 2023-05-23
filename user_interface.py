import time
import pyfiglet

# create a class named 'UserInterface'
class UserInterface:
# create the program title
    def program_title(self): 
        PROGRAM_TITLE = "S I M P L E   C A L C U L A T O R"
        print("\033[1m" + "\033[95m" + pyfiglet.figlet_format(PROGRAM_TITLE.center(70), font= "short"))
        #print short introduction 
        # write for an introduction
        time.sleep(1)
        print("\033[1m" + "\nWelcome to SIMPLE CALCULATOR.") 
        time.sleep(1)
        print("\nPlease input the following requirements to calculate for the resulting value.")

# create a method that asks for user input
    def user_input(self):
         # create a while loop
        while True:
	        # try asking the user to input two numerical values.
            try:
                time.sleep(1)
                value_input = float(input("\nInput the numerical value: "))
                # break the loop if inputs are valid
                return value_input
	        # use except function to capture any Value Error
            except ValueError:
                print("\033[31m" + "\nInvalid Input, input numerical characters only.\n")
                print("\033[95m" + "Please try again.\n")

