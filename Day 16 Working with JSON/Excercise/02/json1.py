import json

data={
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "price": 10.99 
}

with open("books.json","w") as file:
    json.dump(data,file,indent=4)
    print("JSON file created successfully")

with open("books.json","r") as file:
    data=json.load(file)

print("Data from json file read successfully") 
print(data)