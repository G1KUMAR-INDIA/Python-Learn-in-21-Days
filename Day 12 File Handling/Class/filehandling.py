# Opening a File
# file=open("C:\\Users\\G1KUM\\OneDrive\\Desktop\\Mind2i\\00.Class\\Day 12\\Test.txt","r",-1)
# CRUD: Create, Read, Update, Delete
# Read
# gettext=file.read()
# print(gettext)  
# file.close()
# for gettxt in gettext:
#     print(gettxt)

# Create
# file=open("C:\\Users\\G1KUM\\OneDrive\\Desktop\\Mind2i\\00.Class\\Day 12\\Write.txt","w",-1)
# gettext=file.read()
# print(gettext)  
# file.write("Hello World")
# file.close()
# text=["Hello","World"]
# file.writelines("Hello World")
# file.close()

# Update
# file=open("C:\\Users\\G1KUM\\OneDrive\\Desktop\\Mind2i\\00.Class\\Day 12\\Write.txt","a",-1)
# file.writelines("")
# file.close()

# Delete
# import os
# os.remove("C:\\Users\\G1KUM\\OneDrive\\Desktop\\Mind2i\\00.Class\\Day 12\\Write.txt")

# With Statement
with open("C:\\Users\\G1KUM\\OneDrive\\Desktop\\Mind2i\\00.Class\\Day 12\\Test.txt","r",-1) as file:
    gettext=file.read()
    print(gettext)
