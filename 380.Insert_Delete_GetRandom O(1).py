class RandomizedSet:

    def __init__(self):
        self.numMap = {}                            # create a hashmap to store val and key
        self.numList = []                           # create a list to store val

    def insert(self, val: int) -> bool:
        res = val not in self.numMap                # when val not in numMap, return True
        if res:                                     # if val not in numMap
            self.numMap[val] = len(self.numList)    # add val and its key to hashMap
            self.numList.append(val)                # add val to numList
        return res

    def remove(self, val: int) -> bool:
        res = val in self.numMap                    # when val in numMap, return True
        if res:                                     # if val in numMap 
            idx = self.numMap[val]                  # exmple: numMap={1,2,3}, numList=[1,2,3],remove val=2; idx=1,lastVal=3 
            lastVal = self.numList[-1]              # remove val in numList,and move the lastVal to its position,numList[1]=3 and then delete 3 in numList
            self.numList[idx] = lastVal             # copy the numList's lastval to numList[idx]
            self.numList.pop()                      # delete lastVal in numList
            self.numMap[lastVal] = idx              # numMap[3] link to 1 in the numList
            del self.numMap[val]                    # delete val in numMap
        return res

    def getRandom(self) -> int:
        return random.choice(self.numList)          # random.choice() is to find a random item from the list


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
