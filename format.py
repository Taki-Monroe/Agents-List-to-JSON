import json

my_dict = {}

with open("agents.json", "r") as f:
  a = f.read()
  agents = json.loads(a)

for i in agents:
  new = i.split(" - ")
  agent_id = new[0]
  team = new[1]
  name = new[2]
  
  info = {agent_id : {"team": team, "name": name}}
  my_dict.update(info)

print(my_dict)

with open("new.json", "w") as f:
  new_json = json.dumps(my_dict, indent=4)
  f.write(new_json)
