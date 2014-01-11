import glob
import subprocess
import os

INPUT_DIR = '200_(.SBP)'
OUTPUT_DIR = '200_(.SBP)'

Z_Translate = 0 #float(raw_input('\n Enter dZ for translation: \n\n >>> '))

for filepath in glob.glob(INPUT_DIR + '/*.sbp'):
    if filepath[11] == 'B':
        output_filename = filepath.replace('200_(.SBP)\\B200_(.SBP_' , '')
        output_filename = output_filename.replace(').sbp', '')
        output_filepath = str(OUTPUT_DIR + '/A200_(.SBP_' + output_filename + ').sbp')
        with open(filepath, 'r') as f:
            data = []
            for line in f:
                data.append([x.strip() for x in line.strip().split(',')])
        #output_filepath = filepath + '.sbp'
        with open(output_filepath, 'w') as f:
            for element in data:
                if element[0] == 'J3' or element[0] == 'M3':
                    f.write(', '.join(element[:-1]) + ', ' + str(float(element[-1])+Z_Translate) + '\n')
                else:
                    f.write(', '.join(element) + '\n')
            #os.startfile(output_filepath, 'open')
    else:
        continue