theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:

def wikiOrWoko(number):
    if number==0:
        return "woko"
    elif number==1:
        return "wiki"

out_list= list(map(wikiOrWoko,theBools))
print(out_list)