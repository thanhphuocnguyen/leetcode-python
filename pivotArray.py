class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        lt, gt = 0, n - 1
        ans = [pivot] * n
        i, j = 0, n-1
        while(i < n):
            ans[i] = pivot
            if nums[i] < pivot:
                ans[lt] = nums[i]
                lt+=1
            if nums[j] > pivot:
                ans[gt] = nums[j]
                gt-=1
            i+=1
            j-=1
        return ans
