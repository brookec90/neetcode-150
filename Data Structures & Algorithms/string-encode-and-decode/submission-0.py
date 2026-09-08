class Solution:

    def encode(self, strs: List[str]) -> str:
        # empty string to store encoded result
        result = ""     

        # add word length + seperator + actual word
        for word in strs:
            result += str(len(word)) + "#" + word

        return result

    def decode(self, s: str) -> List[str]:
        # list to store words as we recover them
        result = []
        i = 0

        # iterate through encoded string until we reach the end
        while i < len(s):
            j = i

            # if character is not hashtag then keep searching
            while s[j] != "#":
                j += 1

            # gets length of next word 
            length = int(s[i:j])
            
            # extract word and add to result list
            result.append(s[j + 1 : j + 1 + length])

            # move i to start of next encoded word
            i = j + 1 + length
        
        return result

