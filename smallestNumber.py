class Solution:
    def smallestNumber(self, pattern: str) -> str:
        self.result = []
        self.buildSequence(pattern, 0, 0)
        return "".join(self.result[::-1])

    def buildSequence(self, currIdx: int, currCnt: int, pattern: str) -> int:
        if currIdx != len(pattern):
            if pattern[currIdx] == "I":
                self.buildSequence(currIdx + 1, currCnt + 1, pattern)
            else:
                currCnt = self.buildSequence(currIdx + 1, currCnt, pattern)
        self.result.append(str(currCnt))

        return currCnt + 1
