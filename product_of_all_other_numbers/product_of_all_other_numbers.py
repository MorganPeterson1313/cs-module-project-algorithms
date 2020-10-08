'''
Input: a List of integers
Returns: a List of integers
'''
from functools import reduce  
import operator

def product_of_all_other_numbers(arr):
    # Your code here
    my_new_list = []
    
    #loop through h array
    for i in range(0, len(arr), len(arr)):
    #if it is not equal to th item in that index
        if i != len(arr)-1:
    #multiply the things in the numbers in the array
            b = reduce(operator.mul, arr, 1)
            #product_of_all_other_numbers(i)
    # append that number into a new array 
            my_new_list.append(b)
    # return the array
            return my_new_list


# if __name__ == '__main__':
#     # Use the main function to test your implementation
#     # arr = [1, 2, 3, 4, 5]
#     arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

#     print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}"):
