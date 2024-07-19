"""
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.



Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
"""


class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        cols = len(matrix[0])

        row_minimums = [10**5 + 1 for _ in range(rows)]
        col_maximums = [0 for _ in range(cols)]

        for row_ind in range(rows):
            for col_ind in range(cols):
                el = matrix[row_ind][col_ind]
                row_minimums[row_ind] = min(row_minimums[row_ind], el)
                col_maximums[col_ind] = max(col_maximums[col_ind], el)

        lucky_numbers = []
        for row_ind in range(rows):
            for col_ind in range(cols):
                el = matrix[row_ind][col_ind]
                if el == row_minimums[row_ind] == col_maximums[col_ind]:
                    lucky_numbers.append(el)

        return lucky_numbers
