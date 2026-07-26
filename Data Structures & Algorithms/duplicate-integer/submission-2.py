class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set() #creates empty set

        for i in nums:
            if i in hashset: #iterate through loop, have we already seen i in hashset?
                return True  # duplicate found, return True
            hashset.add(i)   # remember this num i for future checks
        return False        
        