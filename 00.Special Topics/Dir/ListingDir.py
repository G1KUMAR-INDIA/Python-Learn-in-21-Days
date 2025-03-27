import os
data=dir(os)
with open("os.txt",'w') as file:
    for i in data:
        file.write(i)
        file.write('\n')
    print("data written to file")