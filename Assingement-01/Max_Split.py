s = input()
cnt = 0;
result = []
temp = ''

for char in s:
    temp += char
    if char == 'R':
        cnt += 1
        # print(cnt,' ',char)
    else : # if char = 'L'
        cnt -= 1
    if(cnt == 0):
        result.append(temp)
        temp = ""
print(len(result))
for stringVal in result:
    print(stringVal)