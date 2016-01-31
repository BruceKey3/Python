import sys

class Solution(object):
    def pascal(self, list, numRows, level):
        if(level > numRows):
            return
        newList = [1]
        if level > 1:
            prevLevel= list[level-2]
            for i  in range(1, level - 1):
                res = prevLevel[i-1] + prevLevel[i]
                newList.append(res)
            newList.append(1)
        list.append(newList)
        self.pascal(list, numRows, (level+1))
    
    def generate(self, numRows=5):
        returnList = []
        self.pascal(returnList,numRows,1)
        return returnList

solution = Solution()
if(len(sys.argv) == 2):
    try:
        list = solution.generate(int(sys.argv[1]))
    except ValueError:
        print("Please call the program with an integer.")
        exit(-1)
else:
    list = solution.generate()
    
for i in list:
    print(i)
