# 485. Max Consecutive Ones. Leetcode
def findMaxConsecutiveOnes(nums):
        max_ones, max_cur = 0, 0
        for i in nums:
            if i:
                max_cur += 1
            else:
                max_ones = max(max_ones, max_cur)
                max_cur = 0

        return max(max_ones, max_cur)

print(findMaxConsecutiveOnes([1,0,0,1,1,1]))