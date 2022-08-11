"""
LinkedIn: https://www.linkedin.com/in/mochi-momo/
github: https://github.com/mochi-momo
YouTube: https://www.youtube.com/channel/UCn2KHtlnvJNd3oRqH7tMjkg
email: emailtomohitsingh@gmail.com
Instagram: @mohit_was_here
"""
### Simple solution
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        out = []
        for acc in accounts:
            out.append(sum(acc))
        return max(out)

### Simple solution with one-line return statement
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(acc) for acc in accounts)
