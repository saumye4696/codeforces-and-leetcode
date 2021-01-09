class Solution:
    def maximumWealth(self, accounts):
        sum, final1 = 0, 0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                sum += accounts[i][j]
            if sum > final1:
                final1 = sum
            sum = 0
        print(final1)
        return final1

Solution().maximumWealth([[1,2,3],[1,2,3]])