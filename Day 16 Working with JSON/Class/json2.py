import json

with open("data.json","r") as file:
    data=json.load(file)

print("Data from json file read successfully") 
print(data)