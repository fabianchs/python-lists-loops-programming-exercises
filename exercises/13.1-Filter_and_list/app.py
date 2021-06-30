
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:

def separate(names):
    return names[0]=="R"

resulting_names= list(filter(separate,all_names))

print(resulting_names)




