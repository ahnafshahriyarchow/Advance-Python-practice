
import sys
import numpy as np

def generate_star_shape(n,s):

    if (n<5):
        print("Value Error: provided value of the side is " , n , " minimum value is 5!" )
        sys.exit(1)

    rows, cols = n,n
    char = s

    square = np.full((rows, cols), ' ', dtype=str)

    square[0, :] = char
    square[:, 0] = char
    square[-1, :] = char
    square[:, -1] = char


    for i in range(1, n-1):
        square[i, i] = char
        square[i, n-i-1] = char

    ctr = np.count_nonzero(square == s)
    
    return ctr, square