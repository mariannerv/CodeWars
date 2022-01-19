def isogram(words):
    res = []
    for x in words:
        if x not in res:
            res.append(x)
    return ''.join(res) == words
