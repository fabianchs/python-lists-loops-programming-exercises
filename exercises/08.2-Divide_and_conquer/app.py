list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list(numbers):
    result=[]
    odd_list=[]
    even_list=[]

    for number in numbers:
        if number%2==0:
            even_list.append(number)
        else:
            odd_list.append(number)
    
    result.append(odd_list)
    result.append(even_list)

    return result

print(merge_two_list(list_of_numbers))

