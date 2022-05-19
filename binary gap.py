#A binary gap within a positive integer N is any maximal sequence of consecutive zeros 
#that is surrounded by ones at both ends in the binary representation of N.

#For example, given N = 1041 the function should return 5, 
#because N has binary representation 10000010001 and so its longest binary gap is of length 5. 
#Given N = 32 the function should return 0, 
#because N has binary representation '100000' and thus no binary gaps.




def solution(N):     
    br = str(bin(N))[2:]
    bin_num_group = False
    bin_num_highest = 0
    bin_zero_counter = 0
    for char in br:
        if char == '1':
            if bin_num_highest < bin_zero_counter:
                bin_num_highest = bin_zero_counter
            bin_num_group = True
            bin_zero_counter =0
        elif bin_num_group:
            bin_zero_counter +=1
    return bin_num_highest
pass