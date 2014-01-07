import glob
import subprocess
import os

input_dir = '102_(LOOPS)'

z_translate = float(raw_input('Enter dZ for translation: \n\n >>>'))

for filename in glob.glob(input_dir + '/*.sbp'):
    with open(filename, 'r') as f:
        data = []
        for line in f:
            data.append([x.strip() for x in line.strip().split(',')])
    write_test = filename + '.translated'
    with open(write_test, 'w') as f:
        for element in data:
            if element[0] == 'J3' or element[0] == 'M3':
                f.write(', '.join(element[:-1]) + ', ' + str(float(element[-1])+z_translate) + '\n')
            else:
                f.write(', '.join(element) + '\n')
        #os.system(str(write_test))
        os.startfile(write_test, 'open')
