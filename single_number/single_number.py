'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    arr.sort()
    #loop through items in array
    #compare the items as if we are sorting them
    #if it is different
    #return the item that is not equal to the others
    
    # for i in arr:
    #     my_list = iter([arr])
    #     x = next(my_list)
    #     for i in x:
    #         if i != item and item != 0:
    #             return x[item]
    for i in range(0, len(arr), 2):
        if arr[i] != arr[i+1]:
            return arr[i]
            
            #if i == len(arr) - 1:

    
                #return arr[i]
        



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(single_number(arr))