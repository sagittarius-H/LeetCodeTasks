class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_sequence = 0
        cur_sequence = 0
        for index, item in enumerate(nums):
            if item == 1:
                cur_sequence += 1
            if item == 0 or index == len(nums) - 1:
                if cur_sequence > max_sequence:
                    max_sequence = cur_sequence
                cur_sequence = 0
        return max_sequence


sol = Solution()
print(sol.findMaxConsecutiveOnes([1,0,1,0,0,1]))