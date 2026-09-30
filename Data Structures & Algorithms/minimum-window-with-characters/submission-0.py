class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}
        left = 0
        have = 0
        required = len(need)

        ans = ""
        ans_len = float("inf")

        for right in range(len(s)):
            c = s[right]

            if c in need:
                window[c] = window.get(c, 0) + 1

                if window[c] == need[c]:
                    have += 1

            while have == required:
                if right - left + 1 < ans_len:
                    ans_len = right - left + 1
                    ans = s[left:right + 1]

                c = s[left]

                if c in need:
                    window[c] -= 1

                    if window[c] < need[c]:
                        have -= 1

                left += 1

        return ans