import datetime


people = [
	{ "name": 'Joe', "birthDate": datetime.datetime(1986,10,24) },
	{ "name": 'Bob', "birthDate": datetime.datetime(1975,5,24) },
	{ "name": 'Erika', "birthDate": datetime.datetime(1989,6,12) },
	{ "name": 'Dylan', "birthDate": datetime.datetime(1999,12,14) },
	{ "name": 'Steve', "birthDate": datetime.datetime(2003,4,24) }
]


def calculateAge(people):
    birthDate= people["birthDate"]
    today = datetime.date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

name_list = list(map(lambda person:  person["name"] , people))
ages_list= list(map(calculateAge, people))
final_list=[]
for i in range(0, len(name_list),1):
    final_list.append("Hello, my name is "+name_list[i]+" and I am "+str(ages_list[i])+" years old")

print(final_list)

