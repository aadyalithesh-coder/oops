class IOS_string():
    def __init__(self):
        self.str1=""

    def getstring (self):
        self.str1= input("Enter string:")

    def print_string(self):
        print("result is:", self.str1.upper())

str1=IOS_string()
str1.getstring()
str1.print_string()