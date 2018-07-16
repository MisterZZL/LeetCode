#详细参考可以看书影博客：http://bookshadow.com/weblog/2015/06/03/leetcode-contains-duplicate-iii/
#方法一：主要是看解题思路：
"""
		|nums[j]−nums[i]|<=t
===>	|nums[j]/t−nums[i]/t|<=1
===>	|floor(nums[j]/t)−floor(nums[i]/t)|<=1
===>	floor(nums[j]/t)∈{floor(nums[i]/t−1,floor(nums[i]/t),floor(nums[i]/t)+1}

如果
		floor(nums[j]/t)不属于{floor(nums[i]/t−1,floor(nums[i]/t),floor(nums[i]/t)+1}

, 则|nums[j]−nums[i]|<=t不成立。

"""
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        dicts = collections.OrderedDict()

        for i in range(len(nums)):
            key = nums[i] / max(1,t)
            for m in (key - 1,key,key + 1):
                if m in dicts and abs(nums[i] - dicts[m]) <= t:
                    return True
            dicts[key] = nums[i]
            if i >= k:
                dicts.popitem(last = False)
        return False
		
#方法二：思路
"""
因为没有重复，所以不能用hash。坐标之差在一个范围内，我们可以每次只在这个范围内寻找数，比如：
从左往右移动，当长度大于k，那么就把搜索区间的最左边删除；
"""

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
	lenth = len(nums)
        a = set()
        for i in range(lenth):
            if t==0:
                if nums[i] in a:
                    return True
            else:
                for atem in a:
                    if abs(nums[i]-atem)<=t:
                        return True
            a.add(nums[i])
            if len(a) == k+1:
                a.remove(nums[i-k])
        return False

"""
这个解法超时；
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if len(nums) == 0 or t < 0:
            return False
        d = {nums[0]: 0}
        for i in range(1, len(nums)):
            if nums[i] in d:
                if abs(i-d[nums[i]]) <= k:
                    return True
                else:
                    d[nums[i]] = i
                    continue
            l = sorted(d.keys())[::-1]
            j = 0
            while j < len(l):
                if abs(nums[i] - l[j]) <= t:
                    if -k <= i - d[l[j]] <= k:
                        return True
                j+=1
            d[nums[i]] = i
        return False
"""