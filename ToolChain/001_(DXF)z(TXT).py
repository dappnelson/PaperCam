from ConfigParser import SafeConfigParser
from Tkinter import Tk
from tkFileDialog import askopenfilename

INI_path = '001_(DXF)z(TXT)config.ini'
config = SafeConfigParser()
config.read(INI_path)
input_path = config.get('stored', 'input_path')
output_path = config.get('stored', 'output_path')
#print input_path 
#print output_path
	
############################################################ handle INPUT PATH
print'\ncurrent Input Path:\n\n>>>', input_path
x = raw_input('\nAccept default Input Path <enter> \nor Browse for new Input Path <\'N\'>\n\n>>>')

if x == 'n' or x == 'N':
	Tk().withdraw() # keeps the root window from appearing
	AAA = askopenfilename() # show "Open" dialog and return Path
	input_path = str(AAA)
	print '\n>>>', input_path
	print '\n\n'
	#raw_input()
else:
	input_path = str(input_path)
	print '\n'
	#raw_input()

############################################################ process INPUT PATH contents, save to 'GCODE'
with open(input_path, "r") as f_111:
	#*processing
	GCODE = f_111.readlines()
	GCODE = list(GCODE)
	#print GCODE
	#raw_input()

############################################################ handle OUTPUT PATH
print'current Output Path:\n\n>>>', output_path
y = raw_input('\nAccept default Output Path <enter> \nor Browse for new Output Path <\'N\'>\n\n>>>')

if y == 'n' or x == 'N':
	Tk().withdraw() # keeps the root window from appearing
	BBB = askopenfilename() # show "Open" dialog and return Path
	output_path = str(BBB)
	print '\n>>>', output_path
	print '\n\n'
	raw_input()
else:
	input_path = str(input_path)
	print '\n'
	#raw_input()
	
############################################################ write 'GCODE' to .TXT
with open(output_path, "w") as f_222:
	for line in GCODE:
		f_222.write(line)
#raw_input()

############################################################ store INPUT_PATH, OUTPUT_PATH to .INI
config.set('stored','input_path', input_path)
config.set('stored','output_path', output_path)
with open(INI_path, 'wb') as configfile:
    config.write(configfile)
print 'Any browsed-for Paths have been stored.\n'






























