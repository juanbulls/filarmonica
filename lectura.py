import json
from pprint import pprint
with open(r"2011light.json") as f:
	datos=json.load(f)
	pprint(data)
print("se va a leer: \n orchestra\n del primer\n programs\n asi: miniProgramas[programs][0][id] omitiendo comillas")
resultado=data["programs"][0]["orchesta"]
input(resultado+"\nSalir?")