from typing import List


def broken_search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_value = nums[mid]
        if mid_value == target:
            return mid
        if nums[left] == target:
            return left
        if nums[left] <= nums[mid]:
            if nums[left] <= target < mid_value:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if mid_value < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
