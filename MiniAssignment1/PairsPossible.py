from MiniAssignment1 import StringClass


class PairsPossible(StringClass):

    def possible(self):

        self.string2=input("enter the string")
        self.result = [(self.string1[i], self.string2[j]) for i in range(0, len(self.string1)) for j in range(0, len(self.string2))]
        print(self.result)


# obj3 = PairsPossible()
# obj3.strlen()
# obj3.strToChar()
# obj3.possible()