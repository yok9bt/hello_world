import json

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

print(json.dumps(sampleJson, indent=2, separators=(",", " = "), sort_keys=True))