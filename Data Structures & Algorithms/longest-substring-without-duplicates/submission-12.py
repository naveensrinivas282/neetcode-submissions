class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        mx=0
        left = 0
        right=0
        for right in range(len(s)):
            while s[right] in st:
                st.remove(s[left])
                left+=1
            st.add(s[right])
            le = right - left + 1
            if le > mx:
                mx = le       
        return mx

            