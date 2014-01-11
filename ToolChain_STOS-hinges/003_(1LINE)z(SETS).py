import os

input_path = '002_(1LINE).txt'
output_path = '004_(SETS).txt'

d1 = 'points = '
d2 = ', '

with open(input_path, "r") as f: #take 3-tuple part 3, after partitioning by d1
    with open(output_path, "w") as g:
        for line in input_path:
            Data = f.readline()
            Data = str(Data)
            print Data
            post_d1 = Data.partition(d1)[2]
            g.write(post_d1) #write to output_path

with open(output_path, "r") as h: #take 3-tuple part 1, after partitioning by d2
    Data = h.readline()
    Data = str(Data)
    print Data
    pre_d2 = Data.partition(d2)[0]

with open(output_path, "w") as h: #overwrite to output_path
    h.write(pre_d2)
	
os.startfile(output_path, 'open')