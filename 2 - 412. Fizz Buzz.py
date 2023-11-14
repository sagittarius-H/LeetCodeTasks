class Solution(object):
    def fizzBuzz(self, n):
        out = [""] * n
        for i in range(0, n):
            if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                out[i] = "FizzBuzz"
            elif (i + 1) % 3 == 0:
                out[i] = "Fizz"
            elif (i + 1) % 5 == 0:
                out[i] = "Buzz"
            else:
                out[i] = str(i+1)
        return out


sol = Solution()
print(sol.fizzBuzz(5))