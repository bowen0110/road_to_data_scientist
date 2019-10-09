# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding 
# another solution using the divide and conquer approach, which is more subtle.

''' 
Solution 1:
brutal force solution 
[1, -2, 23, 4, 5, 2, 23, 5, -23, -4, 523, 5]
--
------
----------
--------------
-----------------
----------------------
---------------------------
-------------------------------
------------------------------------
----------------------------------------
--------------------------------------------

at each index, get all sums of subarrays starting at this index
put the max of window_sum into a max sum list for each index
return the max
running time: O(n^2)
space: O(n)


from typing import List

def max_sub_array(nums: List[int]) -> int:
    n = len(nums) # O(1)

    maxsum_each_ndx = [] # O(1)
    for i in range(n): # outter for loop depends on the inner for loop
        window_sum = [] # O(1)
        for j in range(i, n): # for loop will execute n, n-1, n-2, n-3,...,1 which is total of O(n^2)
            window_sum.append(sum(nums[i:j])) # O(1)
        maxsum_each_ndx.append(max(window_sum)) # O(1)

    return max(maxsum_each_ndx) # O(1)

print(max_sub_array([-3, 4, -2, 23, 4, 23, 4, 5, -1223, 23, 121324, 53534, -13024]))
'''

'''
Solution 2:
Dynamic Programming solution
nums = [1, -2, 23, 4, 5, 2, 23, 5, -23, -4, 523, 5]
temp = [_, __, __, _, _, _, __, _, ___, __, ___, _]

ndx = 1
1
ndx = 2
-2+1 = max(-2, -2+1)
ndx = 3
23 = max(23, -2+1+23)
ndx = 4
4+23 = max(4, 4+23)

create a list with same length as nums
at each position i
compute the sum the of max sub list before + num[i]
compare with num[i]
store the bigger at temp[i]
return the max of temp

running time: o(n)
space: o(n)


from typing import List

def max_sub_array(nums: List[int]) -> int:
    n = len(nums) # o(1)
    temp = nums # o(1)
    for i in range(1, n): # o(n)
        temp[i] = max(nums[i], nums[i]+temp[i-1]) # o(1)
    return max(temp) # o(1)

print(max_sub_array([-3, 4, -2, 23, 4, 23, 4, 5, -1223, 23, 121324, 53534, -13024]))
'''

'''
Solution 3:
Dynamic Programming solution improve space
nums = [1, -2, 23, 4, 5, 2, 23, 5, -23, -4, 523, 5]
temp = [_, __, __, _, _, _, __, _, ___, __, ___, _]

ndx = 1
1
ndx = 2
-2+1 = max(-2, -2+1)
ndx = 3
23 = max(23, -2+1+23)
ndx = 4
4+23 = max(4, 4+23)

create a list with same length as nums
at each position i
compute the sum the of max sub list before + num[i]
compare with num[i]
store the bigger at temp[i]
return the max of temp

running time: o(n)
space: o(1)
'''

from typing import List

def max_sub_array(nums: List[int]) -> int:
    n = len(nums) # o(1)
    max_sum = nums[0] # o(1)
    result = max_sum # o(1)
    for i in range(1, n): # o(n)
        max_sum = max(nums[i], nums[i]+max_sum) # o(1)
        result = max(result, max_sum) # o(1)
    return result # o(1)

print(max_sub_array([-3, 4, -2, 23, 4, 23, 4, 5, -1223, 23, 121324, 53534, -13024]))



