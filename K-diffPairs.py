# October Leetcode challenge

class Solution:
    def findPairs(self, nums, k):           # return int
        l = []
        for i in nums:
            for j in nums:
                if i - j == k or j - i == k: 
                    l.append([i, j])
        count = 0
        print(l)
        for i in range(len(l)):
            count += 1

        return count

s = Solution()
nums = [1,3,1,5,4]
k = 0
print(s.findPairs(nums , k))