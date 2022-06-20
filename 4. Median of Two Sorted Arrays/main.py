class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        all_nums = []
        all_nums.extend(nums1)
        all_nums.extend(nums2)
        all_nums.sort()
        length = len(all_nums)
        if length % 2 == 1:
            return all_nums[int(length / 2)]
        else:
            return (all_nums[int(length / 2)] + all_nums[int((length / 2) - 1)]) / 2

solution = Solution()
print(solution.findMedianSortedArrays([1, 3], [2]))
print(solution.findMedianSortedArrays([1, 2], [3, 4]))
