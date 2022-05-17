class PairsPossible:

    def __init__(self):

        self.name = input("enter the string to be form pairs: ")

    def formingPairs2(self):
        self.newlst = [1, 2]
        self.finallst=[]
        for i in range(1, len(self.name)):
            self.newlst[0] = self.name[i - 1]
            for j in range(0, len(self.name)):
                self.newlst[1] = self.name[j]
                self.finallst.insert(self.newlst)

                # print(self.newlst)
        print(self.finallst)






obj1 = PairsPossible()
obj1.formingPairs2()
