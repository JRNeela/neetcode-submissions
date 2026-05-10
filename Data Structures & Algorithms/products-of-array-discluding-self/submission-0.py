'''
store the prefix product


'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [nums[0]]
        postfixes = [nums[-1]]
        n = len(nums)
        for i in range(1, len(nums)):
            prefixes.append(nums[i] * prefixes[-1])
        for i in range(len(nums) - 2, -1, -1):
            postfixes.append(nums[i] * postfixes[-1])
        ret = [postfixes[len(nums) - 2]]
        for i in range(1, len(nums) - 1):
            ret.append(postfixes[n - i - 2] * prefixes[i - 1])
        ret.append(prefixes[n - 2])
        return ret

        