class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        required = len(t_count)
        window_count = {}
        formed = 0
        l, r = 0, 0
        min_len = float("inf")
        min_window = (0, 0)
        while r < len(s):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            while l <= r and formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_window = (l, r)
                left_char = s[l]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    formed -= 1
                l += 1
            r += 1
        l, r = min_window
        return "" if min_len == float("inf") else s[l:r+1]
