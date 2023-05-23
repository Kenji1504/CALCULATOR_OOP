
# create a class named 'UserInterface'
class UserInterface:
# create a method that asks for user input
    def user_input(self):
         # create a while loop
        while True:
	        # try asking the user to input two numerical values.
            try:
                value_input = float(input("\nInput the first value: "))
                # break the loop if inputs are valid
                return value_input
	        # use except function to capture any Value Error
            except ValueError:
                print("\033[31m" + "\nInvalid Input, input numerical characters only.\n")
                print("\033[95m" + "Please try again.\n")

    def user_input_2(self):
         # create a while loop
        while True:
	        # try asking the user to input two numerical values.
            try:
                value_input = float(input("\nInput the second value: "))
                # break the loop if inputs are valid
                return value_input
	        # use except function to capture any Value Error
            except ValueError:
                print("\033[31m" + "\nInvalid Input, input numerical characters only.\n")
                print("\033[95m" + "Please try again.\n")
                