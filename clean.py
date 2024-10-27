import json
from data import agents

a = agents

lines = a.splitlines()

new_a = []

for line in lines:
  new = line.strip()
  new_a.append(new)
  
with open("new_data.json", "w") as f:
  new_json = json.dumps(new_a, indent=4)
  f.write(new_json)
