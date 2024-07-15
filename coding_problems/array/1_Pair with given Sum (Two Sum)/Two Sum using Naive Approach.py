"""
 The basic approach to solve this problem is by nested traversal.

 Traverse the array using a loop
 For each element:
     Check if there exists another in the array with sum as x
     Return true if yes, else continue
 If no such pair is found, return false.

 Below is the implementation of the above approach
"""

# This python program tells if there exists a pair in array whose sum results in x.

# Function to find and print pair


def chkPair(A, size, x):
    for i in range(0, size-1):
        for j in range(i+1, size):
            if (A[i]+A[j] == x):
                return 1
    return 0


if __name__ == "__main__":
    A = [0, -1, 2, -3, 1]
    x = -2
    size = len(A)

    if (chkPair(A, size, x)):
        print("Yes")

    else:
        print("No")

"""
Time Complexity: O(N2), Finding pair for every element in the array of size N.
Auxiliary Space: O(1)
    """
