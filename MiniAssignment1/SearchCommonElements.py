from PairsPossible import PairsPossible


class SearchCommonElements(PairsPossible):

    def commonElements(self):
        self.string3=input("enter the string")
        common=[]
        for i in range(0,len(self.string1)):
            for j in range(0,len(self.string2)):
                for k in range(0,len(self.string3)):
                    if(self.string1[i] == self.string2[j] and self.string1[i] == self.string3[k]):
                        common.append(self.string1[i])

        print(set(common))



obj3=SearchCommonElements()
obj3.strlen()
obj3.strToChar()
obj3.possible()
obj3.commonElements()
