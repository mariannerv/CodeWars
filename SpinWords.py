def spin_words(sentence):
    
    lista = sentence.split(" ")
    res = []
    for i in lista:
        if len(i) > 5:
            res.append(i[::-1])
        else:
            res.append(i)
    return ' '.join(res)
