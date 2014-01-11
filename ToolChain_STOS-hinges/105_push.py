import json
import glob

INPUT_DIR = '104_(COORD)'
OUTPUT_DIR = '106_(LEADS)'

for filename in glob.glob(INPUT_DIR + '/*.txt'):
    print filename
    output_filename = filename.replace('104_(COORD)\\104_(COORD_' , '')
    output_filename = output_filename.replace(').txt', '')
    output_filepath = str(OUTPUT_DIR + '/106_(LEADS_' + output_filename + ').txt')
    with open(filename, 'r') as f:
        with open(output_filepath , 'w') as g:
            for line in f:
                print line
                g.write(line)
