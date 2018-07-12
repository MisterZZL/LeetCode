class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        r = "{0:032b}".format(n)  #注意转换成32为无符号整形，r=bin(n)在这里会出错，ide不会
        r = r[::-1]
        r = int(r,2)
        return r

if __name__ == '__main__':
	n = 43261596
	s = Solution()
	res = s.reverseBits(n)
	print(res)
