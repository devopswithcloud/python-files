import json
data ={"name":"as","age":30}
with open("data.json","w") as f:
    json.dump(data,f)

#reading a json file 
with open("data.json","r") as f:
    data = json.load(f)
    print(data)