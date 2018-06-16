import json
from pprint import pprint
with open(r"data.json") as f:
	data=json.load(f)
	pprint(data)
print("se va a leer: \n id\n del primer\n maps\n asi: miniProgramas[programs][0][id] omitiendo comillas")
input(data["maps"][0]["id"]+"\nSalir?")