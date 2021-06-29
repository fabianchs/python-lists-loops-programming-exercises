arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:

def sumOdds():
    aux=0

    for number in arr:
        if number%2!=0:
            aux=aux+number

    return aux

print(sumOdds())

