import json

data ={
    "name":"Job",
    "age":25,
    "city":"dhy"
}

#with open('output.json','w') as file:
 #   json.dump(data,file,indent=4)  #indent for pretty formatting

with open('output.json','r') as file:
    data = json.load(file)   # convert JSON to python dict
    print(data['name'])


json_string= '{"name":"A","age":30}'
jdata = json.loads(json_string) # loads  load string
print(jdata['name'])

json_string1 = json.dumps(data)
print(json_string1)