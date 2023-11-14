class Solution(object):
    def numberOfSteps(self, num):
        steps = 0
        while num != 0:
            if num % 2 == 0:
                num = num / 2
                steps += 1
            else:
                num -= 1
                steps += 1
        return steps


sol = Solution()
print(sol.numberOfSteps(123))