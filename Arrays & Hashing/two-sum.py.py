"""
# Problem: https://leetcode.com/problems/two-sum/

You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            print(f"Index: {i}, Number: {num}, Seen: {seen}")
            complement = target - num

            if complement in seen:
                print(f"Found complement: {complement} at index {seen[complement]}")
                return [seen[complement], i]
            print(f"Storing number: {num} at index {i}")
            seen[num] = i
            print(f"Updated Seen: {seen}")

        return []

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)  # Output: [0, 1]

    nums = [3,2,4]
    target = 6
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)  # Output: [1,2]

    nums = [3,3]
    target = 6
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)  # Output: [0, 1]