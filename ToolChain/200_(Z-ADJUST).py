import json
import glob
import subprocess
import os

INPUT_DIR = '200_(.SBP)'
OUTPUT_DIR = '200_(.SBP)'

Z_Translate = float(raw_input('\n Enter dZ for translation: \n\n >>> '))

for filename in glob.glob(INPUT_DIR + '/*.sbp'):
    output_filename = filename.replace('200_(.SBP)\\200_(.SBP_' , '')
    output_filename = output_filename.replace(').sbp', '')
    output_filepath = str(OUTPUT_DIR + '/z200_(.SBP_' + output_filename + ').sbp')
    with open(filename, 'r+') as f:
        with open(output_filepath , 'w') as g:
            data = []
            for line in f:
                print line
                #line_cmd, line_points = line.rsplit(', ', 1)
                line_cmd, delimiter, line_points = line.partition(',')
                print line_cmd
                print line_points
                if line_cmd == 'J3' or line_cmd == 'M3':
                    print line
                    data.append(json.loads('[' + line_points + ']')) #data.append(json.loads('[' + line.strip() + ']'))
                else:
                    print 'continuing <enter>  ' + filename
                    raw_input()
                    continue
            for element in data:
                g.write(line_cmd + ', '  + str(element[0]) + ', ' + str(element[1]) + ', ' + str(element[2]+Z_Translate) + '\n')
                element = line.strip()
                print element
        #os.system(str(output_filename))
        #os.startfile(output_filename, 'open')