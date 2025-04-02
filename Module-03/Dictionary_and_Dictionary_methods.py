person = {'name' : 'Shahin Mia','address' : 'Ashulia','Job':'Software Engineer'}
print(person['name'])
print(person.keys()) #print all keys in person
print(person.values()) #print all values in person
person['Gender'] = 'Male' # add key value to dictonary
print(person)

for key,value in person.items():
    print(key,': ',value)