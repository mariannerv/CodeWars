def binary_array_to_number(arr):
    res = 0
    counter = len(arr)-1
    for i in arr: 
        res = res + i*(2**counter)
        counter -=1
        
    return res
