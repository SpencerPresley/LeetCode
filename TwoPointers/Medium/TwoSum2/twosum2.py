from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        tracker = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in tracker:
                return [tracker[complement] + 1, i + 1] # + 1 for 1 based index
            tracker[num] = i
            
"""
Runtime: 94ms (beats 97.09%)
Memory: 17.61mb (Beats 25.39%)

Explanation:

Define tracker dictionary to store the num at the index as the key and the index as the value

Enumerate through the list getting the index and value out of each index
Calculate the complement, as in the number which added with the current one will = target
If the calculated complement is present in the tracker then our current number and the number stored in value of that complement key
will add to target so we return a list comprised of those.

If the complement is not in the tracker then we add our num as a key and add it's index as the value so that if that happens to be
a future numbers complement then the steps above this one will allow the solution to be found
"""

class Solution2:
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1] # + 1 for 1 based indexing
            elif current_sum < target:
                left += 1
            else:
                right -= 1
                
"""
Runtime: 105ms (Beats 59.70%)
Memory: 17.4mb (Beats 57.72%)

Explanation:

This utilizes a two pointer approach. Two pointers start at the first index and the last index of the list.

We assume the list is sorted.

Iterate until left and right pointers match, if they meet we've explored the whole list, 
this could allow to know when the solution doesn't exist, but in this case one always exists.

We calculate the current sum of the two numbers at each left and right index. If they sum to target return the two numbers just
used to get that target value as those are the two we want.

Since the list is sorted in non-decreasing (increasing) order then we know:
if the current sum was < than target then we need to iterate up from the left side to get larger numbers
if the current sum was > target then we to iterate down from the right side to get smaller numbers
Note: the else case checks >= technically, but if current sum = target there would've already been a return so that case will
never be relevant.
"""