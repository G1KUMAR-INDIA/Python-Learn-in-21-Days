import re
data=dir(re)
with open("re.txt",'w') as file:
    for i in data:
        file.write(i)
        file.write('\n')
    print("data written to file")