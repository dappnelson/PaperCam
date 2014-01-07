import json
import glob
import subprocess
import os

INPUT_DIR = '102_(LOOPS)'
OUTPUT_DIR = '104_(COORD)'

for filename in glob.glob(INPUT_DIR + '/*.txt'):
    #print filename
    output_filename = filename.replace('102_(LOOPS)\\102_(LOOPS_' , '')
    #print output_filename
    output_filename = output_filename.replace(').txt', '')
    #print output_filename
    #raw_input()
    output_filepath = str(OUTPUT_DIR + '/104_(COORD_' + output_filename + ').txt')
    with open(filename, 'r') as f:
        with open(output_filepath , 'w') as g:
            data = []
            for line in f:
                print line
                data.append(json.loads('[' + line + ']')) #data.append(json.loads('[' + line.strip() + ']'))
            for element in data:
                g.write(str(element[0]) + ', '  + str(element[3]) + ', ' + str(element[1]) + ', ' + str(element[2]) + '\n')
                element = line.strip()
                #print element
        #os.system(str(output_filename))
        #os.startfile(output_filename, 'open')