#An array A consisting of N integers is given. 
#Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place.
#For example, the rotation of array 3 times A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] 
#(elements are shifted right by one index and 6 is moved to the first place).



def solution(A, K):
    # write your code in Python 3.6
    if(len(A)> 0 ) or ( K >= 0):
        for i in range(0,K):
            lastelement = A[len(A)-1];
            #print(lastelement)
            for j in range(len(A)-1,-1,-1):
                A[j] = A[j-1];   
            A[0] = lastelement
        return A