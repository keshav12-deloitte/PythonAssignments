class StringClass:
    str = ""

    def __init__(self):
        self.string1 = input("enter the string: ")

    def strlen(self):
        print(len(self.string1))

    def strToChar(self):
        str1 = []
        for i in range(0, len(self.string1)):
            # print(self.str[i])
            str1.append(self.string1[i])

        print(str1)



