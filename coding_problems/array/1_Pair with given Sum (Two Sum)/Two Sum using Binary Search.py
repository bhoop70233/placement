"""
Sort the array, then traverse the array elements and perform binary search for (target – a[i]) on the remaining part
"""

"""
Follow the below steps to solve the problem:

Sort the array in non-decreasing order.
Traverse from 0 to N-1
Initialize searchKey = sum – A[i]
If(binarySearch(searchKey, A, i + 1, N) == True
Return True
Return False
Below is the implementation of the above approach:
"""

# Python program to check for the sum
# condition to be satisfied


def binarySearch(A, low, high, searchKey):
    m = 0
    while (low <= high):
        m = (high+low)//2
        # check if searchKey is present at mid
        if (A[m] == searchKey):
            return 1
            # if  searchKey greater,ignore left half
        if (A[m] < searchKey):
            low = m+1
            # if searchKey is smaller ,ignore right half

        else:
            high = m-1

            # if we reach here ,then element was
            # not present
    return 0


def checkTwoSum(A, arr_size, sum):

    # sort the array
    A.sort()
    l = 0
    r = arr_size-1
    # Traversing all element in an array search for searchKey
    i = 0
    while i < arr_size-1:
        searchKey = sum-A[i]
        # calling binarySearch function
        if (binarySearch(A, i+1, r, searchKey) == 1):
            return 1
        i = i+1

    return 0


# Driver program to test the functions
A = [1, 4, 45, 6, 10, -8]
n = 14
if (checkTwoSum(A, len(A), n)):
    print("Yes")
else:
    print("No")

"""
Time Complexity: O(NlogN)
Auxiliary Space: O(1)
"""
