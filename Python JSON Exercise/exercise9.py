import json

jsonData = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

j = json.loads(jsonData)
l = []
for x in j:
    l.append(x['name'])
print(l)
