#This code uses Floyd's Tortoise and Hare (Cycle Detection) algorithm to find the duplicate number in the given list of integers. 
#The comments provide a step-by-step explanation of how the algorithm works.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize two pointers, slow and fast, both pointing to the first element (index 0) of the array.
        slow, fast = 0, 0

        # Phase 1: Detect the intersection point of the two pointers.
        while True:
            # Move slow one step at a time.
            slow = nums[slow]
            
            # Move fast two steps at a time.
            fast = nums[nums[fast]]
            
            # If they meet, it indicates the presence of a cycle, so break the loop.
            if slow == fast:
                break
        
        # Phase 2: Find the start of the cycle (the duplicate number).
        s2 = 0
        while True:
            # Move one pointer from the start and the other from the intersection point at the same speed.
            s2 = nums[s2]
            slow = nums[slow]
            
            # When they meet again, it will be at the start of the cycle, which is the duplicate number.
            if s2 == slow:
                return s2
