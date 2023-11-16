class Solution(object):
    def findNumbers(self, nums):
        even_counter = 0
        digits = 0
        for num in nums:
            while num >= 10:
                num /= 10
                digits += 1
            digits += 1
            if digits % 2 == 0:
                even_counter += 1
                digits = 0
            else:
                digits = 0
        return even_counter


sol = Solution()
print(sol.findNumbers([100000]))