"""
Problem Statement :
    Given a list of non negative integers, arrange them such that they form the largest number.

"""
class larger(str):
    # here we are comparing two elements i.e. a+b & b+a.
    def __lt__(x, y):
        return x + y >  y+x


class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        s = set(A)
        if len(s)==1 and s.pop() == 0:
            return '0'
        else:
            largest_num = ''.join(sorted(map(str, A), key=larger))
            return largest_num


def main():
    s = Solution()
    #l = [10, 2, 4]
    l = [3, 30, 34, 5, 9]
    # l = [0,0,0,0,0]
    print(s.largestNumber(l))


if __name__ == "__main__":
    main()
