# 70. Climbing Stairs. Leetcode
def climbStairs(n):
        one, two = 0, 1
        for _ in range(n):
            one, two = two, one + two
            print(two)
        return two

print(climbStairs(5))