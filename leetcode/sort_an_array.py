from random import randint
from typing import List

class Solution:
    def sortArray(self,nums):
        #Helper function to perform quick sort.
        def quick_sort(left,right):
            #Base case: If the current segment is empty
            if left>=right:
                return

            #Choose a random pivot element from the segment.
            pivot=nums[randint(left,right)]
            #Initialize pointers:
            #'less_than_pointer' marks the end of the segment with elements less than pivot.
            #'current' is used to scan through the list.
            less_than_pointer,greater_than_pointer,current=left-1,right+1,left

            #Iterate until "current "is less than "greater-than_pointer".
            while current<greater_than_pointer:
                if nums[current]<pivot:
                    # move the element to the segment with elements less than pivot.
                    less_than_pointer+=1
                    nums[less_than_pointer],nums[current]=nums[current],nums[less_than_pointer]
                    current +=1
                elif  nums[current]>pivot:
                    # Move the element to the segment with elements greater than pivot.
                    greater_than_pointer-=1
                    nums[greater_than_pointer],nums[current]=nums[current],nums[greater_than_pointer]
                else:
                    # If the current element is equal to the pivot ,move to next element.
                    current+=1
            # Recursively apply quick sort to the segment with elemnet less than pivot.
            quick_sort(left,less_than_pointer)
            #Recursively apply quick sort to the segment with elements greater than pivot.
            quick_sort(greater_than_pointer,right)

        #call the quick_sort function with the initial bounderies of the list
        quick_sort(0,len(nums)-1)
        #Return the sorted list.
        return nums
