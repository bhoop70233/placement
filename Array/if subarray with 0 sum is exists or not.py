# 1. Brute Force Approach
# This approach checks all possible subarrays to see if any of them sum to 0.


def subarray_with_zero_sum_brute_force(arr):
    n = len(arr)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum == 0:
                return True
    return False


# Example usage
arr = [4, 2, -3, 1, 6]
result = subarray_with_zero_sum_brute_force(arr)
print(result)  # Output: True

# 2. Prefix Sum with Hash Set
# This efficient approach uses a hash set to keep track of the prefix sums we have seen so far. If the prefix sum repeats or becomes zero, it indicates a subarray with sum 0.


def subarray_with_zero_sum_hash_set(arr):
    prefix_sum = 0
    seen_prefix_sums = set()

    for num in arr:
        prefix_sum += num
        if prefix_sum == 0 or prefix_sum in seen_prefix_sums:
            return True
        seen_prefix_sums.add(prefix_sum)

    return False


# Example usage
arr = [4, 2, -3, 1, 6]
result = subarray_with_zero_sum_hash_set(arr)
print(result)  # Output: True


# 3. Prefix Sum with Dictionary
# This approach is similar to the hash set method but uses a dictionary to store prefix sums and their corresponding indices, which can be useful for additional functionality such as finding the actual subarray.


def subarray_with_zero_sum_dict(arr):
    prefix_sum = 0
    prefix_sum_indices = {}

    for i, num in enumerate(arr):
        prefix_sum += num
        if prefix_sum == 0:
            return True
        if prefix_sum in prefix_sum_indices:
            return True
        prefix_sum_indices[prefix_sum] = i

    return False


# Example usage


arr = [4, 2, -3, 1, 6]
result = subarray_with_zero_sum_dict(arr)
print(result)  # Output: True
