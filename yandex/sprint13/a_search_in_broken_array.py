# contest ID 88414107
def broken_search(nums, target) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        left_value = nums[left]
        if left_value == target:
            return left
        right_value = nums[right]
        if right_value == target:
            return right
        mid = left + (right - left) // 2
        mid_value = nums[mid]
        if mid_value == target:
            return mid
        if left_value <= mid_value:
            if left_value < target < mid_value:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if mid_value < target < right_value:
                left = mid + 1
            else:
                right = mid - 1
    return -1
