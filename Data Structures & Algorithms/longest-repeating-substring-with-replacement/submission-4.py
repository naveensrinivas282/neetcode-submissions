class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        ans=[]
        freq={}
        for right in range(left, len(s)):
            t = s[right]
            if t in freq:
                freq[t]+=1
            else:
                freq[t]=1
            high=0
            for i in freq.values():
                if i>high:
                    high=i
            if ((right-left+1) - high) <= k:
                ans.append(right-left+1)
            else:
                freq[s[left]]-=1
                left+=1
        return max(ans)