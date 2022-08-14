"""
LinkedIn: https://www.linkedin.com/in/mochi-momo/
github: https://github.com/mochi-momo
YouTube: https://www.youtube.com/channel/UCn2KHtlnvJNd3oRqH7tMjkg
email: emailtomohitsingh@gmail.com
Instagram: @mohit_was_here
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
