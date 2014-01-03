import json
import os

input_path = '004_(SETS).txt'
output_path = '006_(POINTS).txt'


with open(input_path, 'r') as f:
    lines = f.readlines()
    datastring = lines[0].strip()
    data = json.loads(datastring)
print data

with open(output_path, 'w') as g:
    for element in data:
		if not element[0] == 0 and not element [1] == 0  and not element [2] == 0:
			g.write(str(element[0]) + ', ' + str(element[1]) + ', ' + str(element[2]) + '\n')
		
os.startfile(output_path, 'open')