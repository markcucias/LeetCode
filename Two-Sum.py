class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for i, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in map:
                return [i, map[num2]]
            map[num1] = i