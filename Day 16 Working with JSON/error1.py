import json

# python dictionary
invalid_data = '{"name": "John","age": 30}'

try:
    data = json.loads(invalid_data)
    print(data)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")