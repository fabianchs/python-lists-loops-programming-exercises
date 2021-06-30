par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"


counts = {}
#your code go here:

for letter in par:
    lower_letter=letter.lower()
    if lower_letter==" ":
        pass
    elif lower_letter not in counts:
        counts[lower_letter]=1
    elif lower_letter in counts:
        counts[lower_letter]=counts[lower_letter]+1

print(counts)

