contact = {
    "fullname": "Jane Doe",
    "phone": "321-321-4321",
    "email": "test@test.com"
}
#Your code here:
data=contact.keys()
value=contact.values()

for i in contact:
    print(i+" : "+ contact.get(i))