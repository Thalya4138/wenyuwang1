'''class Solution:
    def singleNumber(self, nums):
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1
        for x, times in count.items():
            if times == 1:
                return x
#到这里使用了类、函数、字典的调用和编写的知识点，有点意思
nums = list(map(int,input().split(",")))
n = Solution()
k = n.singleNumber(nums)
print(k)'''

#下面介绍异或
'''
a ^ a = 0
a ^ 0 = a
异或满足交换律和结合律
class Solution:
    def singleNumber(self, nums):
        ans = 0

        for x in nums:
            ans ^= x

        return ans
s'''