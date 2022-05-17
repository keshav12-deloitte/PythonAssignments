class StringClass:
    str = ""

    def __init__(self):
        self.str = input("enter the string: ")

    def strlen(self):
        print(len(self.str))

    def strToChar(self):
        str1 = []
        for i in range(0, len(self.str)):
            # print(self.str[i])
            str1.append(self.str[i])

        print(str1)


obj = StringClass()
obj.strlen()
obj.strToChar()
