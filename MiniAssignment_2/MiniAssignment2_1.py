class DuplicateValues:
    def __init__(self):
        self.count = None
        self.list1 = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]]

    def finding(self):
        for i in self.list1:
            self.listdup=i
            #print(self.listdup)
            for j in range(0,len(self.listdup)):
                self.count=1
                for k in range(j+1,len(self.listdup)):
                    if self.listdup[j] == self.listdup[k]:
                        self.count +=1
                if self.count >= 2:
                    print("{} -> {}".format(self.listdup[j],self.count))


obj=DuplicateValues()
obj.finding()