"""__author__ = "Thanos Floros, strong-programmer.com"
"""


class Calculator:

    # the init function is used to initialize the class
    def __init__(self):
        # in the initialization we are also creating a variable named result and setting its value to 0
        self.result = 0

    # print the result of the operations
    def print_result(self):
        print("Current result is {}".format(self.result))

    # In all the functions below we have three arguments, self (instance of the class)
    # the other two numberA and numberB are the numbers which will be used for the operations
    def add(self, numberA, numberB):
        self.result = numberA + numberB

    def subtract(self, numberA, numberB):
        self.result = numberA - numberB

    def multiply(self, numberA, numberB):
        self.result = numberA * numberB

    def divide(self, numberA, numberB):
        if numberB != 0:
            self.result = numberA / numberB
        else:
            pass


# the way we run this application is "__main__" because it is the main program
if __name__ == '__main__':

    # create a new object my_calculator by calling the class
    my_calculator = Calculator()
    print("The cool calculator!")
    # this means that the program will run indefinitely
    while True:
        # here with the keyword input, we are asking the user to type something in the run tool.
        # it is the actual interaction with the user
        action = input("What should I do? [A]dd, [S]ubtract, "
                       "show [M]ultiply, or [D]ivide?").upper()
        # number should be an integer, that is why the keyword int is here
        numberA = int(input("Input first number for the calculation: "))
        numberB = int(input("Input second number for the calculation: "))
        if action not in "ASMD" or len(action) != 1:
            print("I don't know how to do that")
            continue
        # Depending on what the user has typed, a different action is executed - different function is called
        if action == 'A':
            my_calculator.add(numberA, numberB)
        elif action == 'S':
            my_calculator.subtract(numberA, numberB)
        elif action == 'M':
            my_calculator.multiply(numberA, numberB)
        elif action == 'D':
            my_calculator.divide(numberA, numberB)

        # show the result by calling the function print_result
        my_calculator.print_result()
