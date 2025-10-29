import json


with open('newdata.json','r') as f:
    data =json.load(f)

for emp in data['company']['employees']:
    print(f"ID:{emp['id']},Name:{emp['name']}")