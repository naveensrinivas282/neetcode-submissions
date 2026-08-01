class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        ans = list(count.keys())[:k]
        return ans