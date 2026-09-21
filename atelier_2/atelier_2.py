import sys
import json

with open ("drinks.json", "r") as file:
    data = json.load(file)

print(data)

