input_path = '002_(1-LINE).txt'
output_path = '004_(JSON).txt'
d1 = 'points = '

with open(input_path, "r") as f:
	for line in input_path:
		Data = f.readline()
		Data = str(Data)
		print Data
		#post_d1 = Data.partition(d1)[2]
		#with open(output_path, "w") as g:
		#	g.write(Data)
		with open(output_path, "w") as g:
			g.write(Data)