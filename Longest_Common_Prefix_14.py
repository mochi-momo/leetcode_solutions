"""
LinkedIn: https://www.linkedin.com/in/mochi-momo/
github: https://github.com/mochi-momo
email: emailtomohitsingh@gmail.com
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ''
        smallest = min(strs)
        for x in range(len(smallest)):
            for word in strs:
                if word[x] != smallest[x]:
                    return lcp
            lcp += smallest[x]
        return lcp
