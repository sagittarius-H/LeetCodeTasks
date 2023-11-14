class Solution(object):
    def maximumWealth(self, accounts):
        wealth = [0] * len(accounts)
        for client_indx, client in enumerate(accounts):
            for bank in client:
                wealth[client_indx] += bank
        return max(wealth)


sol = Solution()
print(sol.maximumWealth([[1,5],[7,3],[3,5]]))