class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        bitSet = set(nums)
        self.result = ""
        return self.backtrack(bitSet, len(nums[0]), "")

    def backtrack(self, bitSet: set, n: int, currStr: str) -> str:
        if len(currStr) == n:
            if currStr not in bitSet:
                return currStr
            return None
        result = self.backtrack(bitSet, n, currStr + "0")
        if result != None:
            return result
        result = self.backtrack(bitSet, n, currStr + "1")
        if result != None:
            return result
        return None
