from PairsPossible import PairsPossible


class EqualSumPairs(PairsPossible):

    def pairsWithdistinctSum(self):
        self.count = 0
        for i in range(0,1):
            for index in range(1,2):
                sum = int(self.result[i][index-1]) + int(self.result[i][index])
                for j in range(1, len(self.result)):
                    for index2 in range(1,2):
                        sum1 = int(self.result[j][index2-1]) + int(self.result[j][index2])
                        if sum != sum1:
                            self.count = self.count + 1
                        elif sum == sum1:
                            self.count =self.count - 1

        print(self.count)


obj3 = EqualSumPairs()
obj3.strlen()
obj3.strToChar()
obj3.possible()
obj3.pairsWithdistinctSum()
