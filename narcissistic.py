def narcissistic(value):
    lista = [int(x)**len(str(value)) for x in str(value)]
    return sum(lista) == value 
