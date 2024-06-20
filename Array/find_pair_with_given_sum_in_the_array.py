# 1. Brute Force Approach
# The brute force approach involves checking all possible pairs in the array to see if they sum to the given value.

# def find_pair_brute_force(arr, target_sum):
#     n = len(arr)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if arr[i] + arr[j] == target_sum:
#                 return (arr[i], arr[j])
#     return None

# # Example usage
# arr = [10, 2, 3, 7, 5]
# target_sum = 9
# result = find_pair_brute_force(arr, target_sum)
# print(result)  # Output: (2, 7)


# 2. Hash Set Approach
# This approach uses a hash set to store the elements we have seen so far. For each element, we check if the complement (i.e., target_sum - element) exists in the set.


def find_pair_hash_set(arr, target_sum):
    seen = set()
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return None


# Example usage
arr = [10, 2, 3, 7, 5]
target_sum = 9
result = find_pair_hash_set(arr, target_sum)
print(result)  # Output: (2, 7)

# 3. Two-Pointer Technique
# This approach requires the array to be sorted first. We then use two pointers, one starting at the beginning and the other at the end of the array, and move them towards each other until we find the pair that sums to the target.


def find_pair_two_pointer(arr, target_sum):
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return (arr[left], arr[right])
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1
    return None


# Example usage
arr = [10, 2, 3, 7, 5]
target_sum = 9
result = find_pair_two_pointer(arr, target_sum)
print(result)  # Output: (2, 7)
