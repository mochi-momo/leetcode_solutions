"""
LinkedIn: https://www.linkedin.com/in/mochi-momo/
github: https://github.com/mochi-momo
YouTube: https://www.youtube.com/channel/UCn2KHtlnvJNd3oRqH7tMjkg
email: emailtomohitsingh@gmail.com
Instagram: @mohit_was_here
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        for val in range(1, len(nums)):
            if nums[val] != nums[val-1]:
                nums[count] = nums[val]
                count += 1
        return count
