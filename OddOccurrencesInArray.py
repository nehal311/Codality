#A non-empty array A consisting of N integers is given. 
#The array contains an odd number of elements, and each element of the array can be paired with another element that
#has the same value, except for one element that is left unpaired.


#For example, given array A such that:

#  A[0] = 9  A[1] = 3  A[2] = 9
#  A[3] = 3  A[4] = 9  A[5] = 7
#  A[6] = 9
#the function should return 7, as explained in the example above.


def solution(A):
    s = set()
    for i in A:
        if i in s:
            s.remove(i)
        else:
            s.add(i)
    # print(unpaired)
    ans = s.pop() if len(s) > 0 else 0
    return ans
    pass