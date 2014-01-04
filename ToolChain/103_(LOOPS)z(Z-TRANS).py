import json
import glob
import os

input_dir = '102_(LOOPS)'

z_translate = float(raw_input('Enter dZ for translation: \n\n >>>'))

for filename in glob.glob(input_dir + '/*.txt'):
    write_test = filename + '.test'
    with open(filename, 'r') as f:
        with open(write_test , 'w') as g:
            data = []
            for line in f:
                data.append(json.loads('[' + line.strip() + ']'))
            for element in data:
                g.write(str(element[0]) + ', ' + str(element[1]) + ', ' + str(element[2]+z_translate) + '\n')
                element = line.strip()
                print element
            os.system(str(write_test))
            #os.startfile(write_test, 'open')