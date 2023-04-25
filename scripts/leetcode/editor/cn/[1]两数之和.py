"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。 

 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。 

 你可以按任意顺序返回答案。 

 

 示例 1： 

 
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
 

 示例 2： 

 
输入：nums = [3,2,4], target = 6
输出：[1,2]
 

 示例 3： 

 
输入：nums = [3,3], target = 6
输出：[0,1]
 

 

 提示： 

 
 2 <= nums.length <= 10⁴ 
 -10⁹ <= nums[i] <= 10⁹ 
 -10⁹ <= target <= 10⁹ 
 只会存在一个有效答案 
 

 进阶：你可以想出一个时间复杂度小于 O(n²) 的算法吗？ 

 Related Topics 数组 哈希表 👍 14977 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        if not nums:
            return [-1, -1]

        # # 哈希
        # hash_list = []
        # for index, num in enumerate(nums):
        #     if num in hash_list:
        #         return sorted([index, hash_list.index(num)])
        #
        #     hash_list.append(target - num)
        #
        # return [-1, -1]

        # 双指针
        nums = [(num, index) for index, num in enumerate(nums)]
        nums.sort()

        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left][0] + nums[right][0] > target:
                right -= 1
            elif nums[left][0] + nums[right][0] < target:
                left += 1
            else:
                return sorted([nums[left][1], nums[right][1]])
        return [-1, -1]

# leetcode submit region end(Prohibit modification and deletion)
