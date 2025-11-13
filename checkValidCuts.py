from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xAxisPair = [None] * len(rectangles)
        yAxisPair = [None] * len(rectangles)
        for i in range(0,len(rectangles)):
            xAxisPair[i] = [None]*2
            yAxisPair[i] = [None]*2
            xAxisPair[i][0] = rectangles[i][0]
            xAxisPair[i][1] = rectangles[i][2]
            yAxisPair[i][0] = rectangles[i][1]
            yAxisPair[i][1] = rectangles[i][3]
        
        return self.check(xAxisPair) or self.check(yAxisPair)
    
    def check(self, coords: List[List[int]]) -> bool:
        coords.sort()
        prevEnd = coords[0][1]
        cnt = 0
        for i in range(len(coords)):
            start,end = coords[i][0], coords[i][1]
            if start >= prevEnd:
                cnt+=1
            prevEnd = max(end, prevEnd)
        return cnt >= 1