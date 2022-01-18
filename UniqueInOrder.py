def unique_in_order(iterable):
    res = []

    for i in range(len(iterable)):
        if len(iterable) == 1 or iterable[i] == iterable[i-1] and iterable[i] not in res:
            res.append(iterable[0])
        elif iterable[i] != iterable[i-1]:
            res.append(iterable[i])
        else:
           res = res
    return res
