class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        l = len(prices)
        right = l
        mx=0
        for right in range(l):
            if prices[left] > prices[right]:
                left = right
                print(left, right)
            else:
                mx = max(mx, prices[right] - prices[left])
        return mx