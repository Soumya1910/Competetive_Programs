"""
Problem Statement :
    Given an array of integers, sort the array into a wave like array and return it,
    In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

"""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def swap(self, a,b):
        a = a+b
        b = a -b
        a = a - b
        return a,b

    def wave(self, A):
        A.sort()
        for i in range(len(A)-1):
            if i%2 == 0:
                if A[i] < A[i+1]:
                    A[i], A[i+1] = self.swap(A[i], A[i+1])
            else:
                if A[i] > A[i+1]:
                    A[i], A[i + 1] = self.swap(A[i], A[i + 1])
        return A



def main():
    s = Solution()
    l = [5, 1, 3, 2, 4 ]
    # l = [3, 30, 34, 5, 9]
    # l = [0,0,0,0,0]
    print(s.wave(l))


if __name__ == "__main__":
    main()
