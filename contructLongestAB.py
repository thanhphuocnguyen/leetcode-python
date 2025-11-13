class Solution:
    def longestString(self, AA: int, BB:int, AB: int) -> str:
        ans = ""
        mi = min(AA,BB)
        for _ in range(mi):
            s = "AABB"
            ans+=s
        buffer = ""
        while AB > 0:
            buffer += "AB"
            AB-=1
        AA-=mi
        BB-=mi

        if AA:
            ans +=buffer+"AA"
        elif BB:
            ans = "BB"+ans+buffer
        return ans