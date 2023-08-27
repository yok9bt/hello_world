import json

invalidJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

try:
    json.loads(invalidJson)
except ValueError as e:
    print('bad json:', e)
