import os

input_path = '006_(POINTS).txt'
output_path = '100_(POINTS).txt'


fIn = open(input_path)  # use raw strings for windows file names
fOut = open(output_path, "w")
for line in fIn:
    fOut.write(line)
fIn.close()
fOut.close()

os.startfile(output_path, 'open')