# Function to check if a sublist with zero-sum is present in a given list or not
def hasZeroSumSublist(nums):
    # create an empty set to store the sum of elements of each
    # sublist 'nums[0...i] ' ,where 'o<=i<len(nums)'
    s = set()

    # insert 0 into the set to handle the case when sublist with
    # zero-sum starts from index 0
    s.add(0)

    total = 0

    # traverse the given list
    for i in nums:
        # sum of elements so far
        total += i
        # if the sum is seen before, we have found a sublist with zero-sum
        if total in s:
            return True
        # insert sum so far into the set
        s.add(total)
       # we reach here when no sublist with zero-sum exists
    return False


if __name__ == '__main__':
    nums = [4, -6, 3, -1, 4, 2, 7]
    if hasZeroSumSublist(nums):
        print('Sublist exists')
    else:
        print('Sublist does not exits')
