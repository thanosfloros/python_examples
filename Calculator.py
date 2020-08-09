class Calculator:

    def __init__(self):
        self.result = 0

    def say_state(self):
        print("Current result is {}".format(self.result))

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


if __name__ == '__main__':

    my_calculator = Calculator()
    print("The cool calculator!")
    while True:
        action = input("What should I do? [A]dd, [S]ubtract, "
                 "show [M]ultiply, or [D]ivide?").upper()
        numberA = int(input("Input first number for the calculation: "))
        numberB = int(input("Input second number for the calculation: "))
        if action not in "ASMD" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_calculator.add(numberA, numberB)
        elif action == 'S':
            my_calculator.subtract(numberA, numberB)
        elif action == 'M':
            my_calculator.multiply(numberA, numberB)
        elif action == 'D':
            my_calculator.divide(numberA, numberB)
        my_calculator.say_state()