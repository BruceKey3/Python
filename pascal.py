class Solution(object):
    def pascal(self, list, numRows, level):
        if(level > numRows):
            return
        newList = [1]
        if level > 1:
            print(len(list))
            print(level)
            prevLevel= list[level-2]
            for i  in range(1, level - 1):
                res = prevLevel[i-1] + prevLevel[i]
                newList.append(res)
            newList.append(1)
        list.append(newList)
        self.pascal(list, numRows, (level+1))
    
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        returnList = []
        self.pascal(returnList,numRows,1)
        return returnList

solution = Solution()
list = solution.generate(5)
print(list)
