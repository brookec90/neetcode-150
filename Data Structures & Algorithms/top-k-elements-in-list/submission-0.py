class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create count dictionary to store how many times each num appears
        count = {}

        # iterate through each number and raise count by 1 if we have seen the number
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # find which number has the highest frequency and sort by largest to smallest
        sorted_nums = sorted(count, key = count.get, reverse = True)

        # use list slicing to return k items
        return sorted_nums[:k]