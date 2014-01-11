from ConfigParser import SafeConfigParser
from Tkinter import Tk
from tkFileDialog import askopenfilename
import time

INI_path = '_file-selector_config.ini'
config = SafeConfigParser()
config.read(INI_path)
input_path = config.get('stored', 'input_path')
output_path = config.get('stored', 'output_path')
	
############################################################ handle INPUT PATH
print 'Browse for input file.'
time.sleep(1)

Tk().withdraw() # keeps the root window from appearing
INI_in = askopenfilename() # show "Open" dialog and return Path
input_path = str(INI_in)
print '\n>>>', input_path
print '\n\n'
#raw_input()
	
############################################################ write 'file_in_contents' to file_out
with open(output_path, "w") as file_out:
	for line in file_in_contents:
		file_out.write(line)
#raw_input()

############################################################ store INPUT_PATH, OUTPUT_PATH to .INI
config.set('stored','input_path', input_path)
config.set('stored','output_path', output_path)
with open(INI_path, 'wb') as configfile:
    config.write(configfile)
print 'Any browsed-for Paths have been stored.\n'
raw_input()






























