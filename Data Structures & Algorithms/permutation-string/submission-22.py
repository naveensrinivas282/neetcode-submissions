class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        t=s1
        right=0
        count=0
        while right < len(s2):
            if s2[right] not in t:
                left+=1
                right=left-1
                t=s1
            else:
                t = t.replace(s2[right], "", 1)
            if t =="":
                return True
            right+=1
            count+=1
        return False
            