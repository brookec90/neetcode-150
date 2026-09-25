class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create set to remove duplicates
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # if prev num does not exist then start sequence
            if num - 1 not in num_set:
                length = 1

                # checks for next num in sequence
                while num + length in num_set:
                    length += 1
                
                # keeps track of longest sequence 
                longest = max(longest, length)
        
        return longest
        