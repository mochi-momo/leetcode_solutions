"""
LinkedIn: https://www.linkedin.com/in/mochi-momo/
github: https://github.com/mochi-momo
YouTube: https://www.youtube.com/channel/UCn2KHtlnvJNd3oRqH7tMjkg
email: emailtomohitsingh@gmail.com
Instagram: @mohit_was_here
"""
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        while num > 0:
            if num % 2 == 0:
                num/=2
            else:
                num-=1
            count+=1
        return count

### Same logic but with a one line if/else statement
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        while num > 0:
            num = num / 2 if num % 2 == 0 else num - 1
            count+=1
        return count
