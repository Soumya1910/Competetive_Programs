"""
Problem Statement :
    "Given a non-negative number represented as an array of digits, add 1 to the number. The digits are stored such that the most significant digit is at the head of the list."
"""

import functools
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        a = int(functools.reduce(lambda x,y : str(x)+str(y), A))
        a +=1
        a = str(a)
        return list(a)

def main():
    s = Solution()
    l = [1,2,3,6,9]
    print(s.plusOne(l))

if __name__ == "__main__":
    main()