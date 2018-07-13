# class Solution:
#     def isValid(self,s):
#         if s == "":
#             return True
#         if len(s)==0 or len(s) % 2 ==1:
#             return False
#         d = {"(" :")","[" :"]","{" :"}"}
#         l = []
#         for i in s:
#             if i in d:
#                 l.append(i)
#             else:
#                 if len(l) == 0 or d[l.pop()] != i :
#                     return False
#         if len(l) != 0:
#             return False
#         return True
#
# s = Solution()
# print(s.isValid("(())"))

# nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2,
class Solution:
    def removeElement(self,nums,val):
        for i in nums:
            if i != val:
                nums.pop(i)

        return nums
s = Solution()
t = s.removeElement(nums = [3,2,2,3], val = 3)
print(t)