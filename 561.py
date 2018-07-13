class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = list(nums)
        num.sort()
        count = 0
        for i in range(0,len(num),2):
            count += num[i]
        return count


a = Solution()
nums = [1,4,3,2]
r = a.arrayPairSum(nums)
print(r)
