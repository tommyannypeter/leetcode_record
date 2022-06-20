from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for iii in range(len(nums)):
            try:
                twin = nums.index(target - nums[iii])
                if twin == iii:
                    continue
                ans.append(iii)
                ans.append(twin)
                break
            except ValueError:
                pass
        return ans
