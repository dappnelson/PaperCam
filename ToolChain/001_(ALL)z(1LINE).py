import os

input_path = '000_(ALL).scad'
output_path = '002_(1LINE).txt'
starts_startswith = 'polyhedron'

with open(input_path, "r") as f:
	for line in input_path:
		SCAD = f.readline()
		SCAD = str(SCAD)
		if SCAD.startswith(starts_startswith) is True:
			text_after_d1 = SCAD.partition('[[')[2]
			print SCAD
			with open(output_path, "w") as g:
				g.write(SCAD)
				
os.startfile(output_path, 'open')