# with open('message.txt','w') as file: # write in file
    # file.write('I Love Shahin')

# with open('message.txt','a') as file: # append in file
#     file.write('I Love Shahin So Much')

with open('message.txt','r') as file: # read in file
    text = file.read()
    print(text)