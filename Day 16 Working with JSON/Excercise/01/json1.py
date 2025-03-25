import json
# data={
#     "company": "TechCorp",
#     "employees": [
#         {
#             "name": "Alice",
#             "role": "Developer"
#         },
#         {
#             "name": "Bob",
#             "role": "Designer"
#         },
#         {
#             "name": "Charlie",
#             "role": "Manager"
#         }
#     ]
# }
# creating json
# with open("data.json","w") as file:
#     json.dump(data,file,indent=4)
#     print("JSON file created successfully")

with open("data.json","r") as file:
    data=json.load(file)

print("Data from json file read successfully") 
print(data)