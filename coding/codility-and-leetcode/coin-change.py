# 322. Coin Change. Leetcode
class Solution(object):
    def coinChange(self, coins, amount):
        if amount < 1:
            return 0
        M = [-1] * (amount + 1)

        for c in sorted(coins):
            if c > amount:
                break
            M[c] = 1
            for i in xrange(1, amount+1):
                if i + c > amount:
                    break
                elif M[i] > 0:
                    M[i+c] = min(M[i+c], M[i] + 1) if M[i+c] > 0 else M[i] + 1
        return M[amount]