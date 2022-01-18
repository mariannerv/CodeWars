def check_exam(arr1,arr2):
    res = 0 
    for i, j in zip(arr1, arr2):
            if i == j:
                res += 4
            elif j == "":
                res += 0
            elif i != j:
                res -= 1 
    if res < 0:
        return 0
    return res
