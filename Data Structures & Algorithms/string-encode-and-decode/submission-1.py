class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for i in strs:
            st=st+str(len(i))+"#"+i
        return st # 2#!a

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i < len(s):
            length=""
            j=i
            while s[j]!="#":
                length+=s[j]
                j+=1
            length=int(length)
            temp=s[j+1:j+1+length]
            res.append(temp)
            i+=length+1+len(str(length))
        return res