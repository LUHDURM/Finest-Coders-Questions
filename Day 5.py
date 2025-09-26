class Solution:
    def reverseBits(self, n: int) -> int:
        bit = format(n,'032b')
        revbit = bit[::-1]
        return int(revbit,2)
        
