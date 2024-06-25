class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create a dictionary to track numbers and their index
        num_2_index = {}
        # Iterate over the numbers in the list
        for i in range(len(nums)):
            num = nums[i]
            # Calculate the difference between the current number and target
            difference = target - num
            # If the difference (i.e., the number we are looking for) exists in the num_2_index
            if difference in num_2_index:
                # Return the current index and the index of the other number
                return [i, num_2_index[difference]]
            # Add the number and its index to the dictionary
            num_2_index[num] = i


# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(nums, target))  # Output should be [1, 0]
