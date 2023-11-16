class Solution(object):
    def sortedSquares(self, nums):
        for index, num in enumerate(nums):
            nums[index] = num * num
        return sorted(nums)


sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))