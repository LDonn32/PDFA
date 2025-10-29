# playing with json
# Author: Laura Donnelly

import json
data ={
  'name':'joe',
  'age':21,
  "student": True
 }

with open ("silly.json", "w") as fp:
    json.dump(data,fp, indent= 4)
jsonSting = json.dumps(data)
print (data)
print (jsonSting)