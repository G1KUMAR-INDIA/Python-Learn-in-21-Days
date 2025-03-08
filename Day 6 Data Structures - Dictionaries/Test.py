# dic={'IND':'India','PAK':'Pakistan','AUS':'Australia','ENG':'England'}
# print(dir(dic))
# print(dic['IND'])
# print(dic.keys())
# for i in dic.keys():
#     print(i)
# print(dic.values())
# for i in dic.values():
#     print(i)
# print(dic.items())
# for i in dic.items():
#     print(i)
# for key,value in dic.items():
#     print(f'{key,value}')

employee={
    "name":"Ravi",
    "age":25,
    "department":['research','development']
}
# print(employee['name'])
print(employee.get('name','Not Found'))
employee["salary"]=20000
# print(employee['age'])
# print(employee['department'])
for key,value in employee.items():
    print(f'{key}:{value}')