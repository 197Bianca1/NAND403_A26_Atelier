import sys
import json

json_file = sys.argv[1]
print(json_file )

try:

 file = open(json_file)
 data = json.load(file)
 print(data)
except:
 print(f"could not load data from {json_file}")

