class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set() #creates empty set

        for i in nums:
            if i in hashset: #iterate through loop, have we already seen i in hashset?
                return True  #return True if we have already seen i in hashset
            hashset.add(i)   #if unseen, then store it
        return False        
        