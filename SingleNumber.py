"""
Questions : Given a non-empty array of integers, every elements appears twice except for one. Find that single one.
nums = [4,1,2,1,2]
#expected output is 1
"""


# Approach 1: using default hash, where it gives 0 if number is not available in dictionary, hence no error if key is not available in dictionary.

from collections import defaultdict
nums = [4,1,2,1,2]
def singleNumber(nums):
    hash_table = defaultdict(int)
    for num in nums:
        hash_table[num]  = hash_table[num] + 1
    
    for num in hash_table:
        if hash_table[num] == 1:
            return num, hash_table[num]

num, index = singleNumber(nums)
print(f"element is {num} and index is {index}")