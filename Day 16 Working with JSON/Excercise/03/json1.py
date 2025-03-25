import json
# invalid_json = '{ "name": "John", age: 30 }'
try:
    with open("invalid.json", "r") as file:
        data = json.load(file)
        print("Data from json file read successfully") 
        print(data)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")