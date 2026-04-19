# Define a class which has at least two methods: getString (to get a string from console input) and printString (to print the string in upper case). Also include a simple test.



class TwoMethods(object):

    def __init__(self):
        self.input = ""

    def getString(self):
        self.input = input("Enter a String: ")

    def printString(self):
        print(self.input.upper())

obj = TwoMethods()
obj.getString()
obj.printString()


