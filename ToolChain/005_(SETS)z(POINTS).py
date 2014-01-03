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
    for line in data:
        g.write(str(line[0]) + ', ' + str(line[1]) + ', ' + str(line[2]) + '\n')
		
os.startfile(output_path, 'open')