import json
import glob
import subprocess
import os

INPUT_DIR = '106_(LEADS)'
OUTPUT_DIR = '108_(.SBP)'

for filename in glob.glob(INPUT_DIR + '/*.txt'):
    output_filename = filename.replace('106_(LEADS)\\106_(LEADS_' , '')
    output_filename = output_filename.replace(').txt', '')
    output_filepath = str(OUTPUT_DIR + '/108_(.SBP_' + output_filename + ').sbp') 
    with open(filename, 'r') as f:
        data = []
        for line in f:
            data.append([float(x.strip()) for x in line.strip().split(',')[1:]])

        with open(output_filepath, 'w') as f:
            # HEADER
            #f.write('# add Move Speed, XY-speed = 0.5 in/sec, Z-speed = 0.5 in/sec\n')
            f.write('MS, 0.5, 0.5\n')
            #f.write('# add Jog to (0,0)\n')
            f.write('J2, 0, 0\n')
            #f.write('# add Jog to (above the first point (nextline\'s_X-value, nextline\'s_Y-value, Z-variable))\n')
            first = data[0]
            f.write('J3, ' + str(first[0]) + ', ' + str(first[1]) + ', ' + str(first[2]) + '\n')
            # MAIN CONTENT
            for element in data:
                f.write('M3, '  + str(element[0]) + ', ' + str(element[1]) + ', ' + str(element[2]) + '\n')
            # FOOTER
            #f.write('# add Jog to (above the first point (nextline\'s_X-value, nextline\'s_Y-value, Z-variable))\n')
            f.write('J3, ' + str(first[0]) + ', ' + str(first[1]) + ', ' + str(first[2]) + '\n')
            #f.write('# add Jog to (0,0)\n')
            f.write('J2, 0, 0\n')