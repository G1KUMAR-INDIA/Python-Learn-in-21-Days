import json
# python dictionary:
data ={
    "name": "John",
    "age": 30,
    "skills":["Python","Java","C++"],
    "address":{
        "street":"KVS STREET",
        "city":"Palamaneru",
        "state":"Andhra Pradesh",
        "pincode":517408
    }
}
# convert python dictionary to json string
with open("data.json","w") as file:
    json.dump(data,file,indent=4)
    print("JSON file created successfully")