class Solution:    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        result = []
        temp = []

        def backtrack(i):
            if i == length:
                result.append(temp[:])
                return

            backtrack(i+1)

            temp.append(nums[i])
            backtrack(i+1)
            temp.pop()

        backtrack(0)
        return result
    
