input_path = '004_(JSON).txt'
output_path = '100_(POINTS).csv'


fIn = open(input_path)  # use raw strings for windows file names
fOut = open(output_path, "w")
for line in fIn:
    fOut.write(line)
fIn.close()
fOut.close()