import json
import glob

INPUT_DIR = '108_(.SBP)'
OUTPUT_DIR = '200_(.SBP)'

for filename in glob.glob(INPUT_DIR + '/*.sbp'):
    output_filename = filename.replace('108_(.SBP)\\A108_(.SBP_' , '')
    output_filename = output_filename.replace(').sbp', '')
    output_filepath = str(OUTPUT_DIR + '/A200_(.SBP_' + output_filename + ').sbp')
    with open(filename, 'r') as f:
        with open(output_filepath , 'w') as g:
            for line in f:
                print line
                g.write(line)
