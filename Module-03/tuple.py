#tuple is a muteable collections 
def multupule():
    return 2,3

# print(multupule())

things = 'pen','tripod','water bottle','charger', 'phone'
# print(type(things))
print(things[1])
print(things[1:4])

# things[0] = 'truck' #can't assign value into tuple

for item in things:
    print(item)

mega = ([12,43,43],[43,43,5]) 
mega[1][1] = 57 #but can change tuple has muteable things inside like array or list
print(mega)