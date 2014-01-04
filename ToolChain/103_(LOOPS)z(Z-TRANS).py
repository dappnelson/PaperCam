import json
import glob
import os

input_dir = '102_(LOOPS)'

z_translate = raw_input('Enter dZ for translation: \n\n >>>')

for filename in glob.glob(input_dir + '/*.txt'):
	write_test = filename + '.test'
	with open(filename, 'r') as f:
		with open(write_test , 'w') as g:
			data = []
			for line in f:
				data.append(json.loads('[' + line.strip() + ']'))
			print data
			g.write(str(data) + '\n') #str(element[0]) + str(element[1]) + str(element[2]) + '\n')
			os.startfile(write_test, 'open')

				
				
				
#	for element in data:
#		print data
#		#element = int(element)
#		#g.write(str(element[0]+z_translate) + ', ' + str(element[1]+z_translate) + ', ' + str(element[2]+z_translate) + '\n')
#os.startfile(write_test, 'open')