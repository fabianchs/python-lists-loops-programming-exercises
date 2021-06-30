#Import random
import random
#Create the function below:

def matrixBuilder(number):
    final_matrix={}
    for i in range (0,number,1):
        final_matrix[i]=[]
        for j in range(0,number):
            final_matrix[i].append(1)
    return final_matrix



condition=True
counter=0
result=[]
matrix=matrixBuilder(random.randint(0,10))

while(condition):
    if counter in matrix:
        result.append(matrix[counter])
    elif counter not in matrix:
        condition=False

    counter=counter+1

print(result)
