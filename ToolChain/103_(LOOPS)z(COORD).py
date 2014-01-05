import json
import glob
import subprocess
import os

input_dir = '102_(LOOPS)'

for filename in glob.glob(input_dir + '/*.txt'):
    output_filename = filename.replace('loop_', '')
    output_filename = output_filename.replace('.txt', '')
    output_filename = str(output_filename + '.sbp')
    print output_filename
    with open(filename, 'r') as f:
        with open(output_filename , 'w') as g:
            data = []
            for line in f:
                print line
                data.append(json.loads('[' + line + ']')) #data.append(json.loads('[' + line.strip() + ']'))
            for element in data:
                g.write(str(element[0]) + ', '  + str(element[3]) + ', ' + str(element[1]) + ', ' + str(element[2]) + '\n')
                element = line.strip()
                print element
        #os.system(str(output_filename))
        #os.startfile(output_filename, 'open')