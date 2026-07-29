class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for i in s:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        for i in t:
            if i not in count:
                return False
            else:
                count[i]-=1
        for i in count.values():
            if i!=0:
                return False

        return True