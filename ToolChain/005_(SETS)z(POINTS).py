import json
import os

convert_ratio = 1/25.4 # MM to IN

input_path = '004_(SETS).txt'
output_path = '006_(POINTS).txt'

# read file to array
with open(input_path, 'r') as f:
    lines = f.readlines()
    datastring = lines[0].strip()
    data = json.loads(datastring)
print data

# write element to file as CSV # convert MM to IN
with open(output_path, 'w') as g:
    for element in data:
		if not element[0] == 0 and not element [1] == 0  and not element [2] == 0:
			g.write(str(element[0]*convert_ratio) + ', ' + str(element[1]*convert_ratio) + ', ' + str(element[2]*convert_ratio) + '\n')
		
os.startfile(output_path, 'open')