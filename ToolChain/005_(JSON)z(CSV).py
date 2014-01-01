input_path = '004_(JSON).txt'
output_path = '006_(CSV).txt'
#d1 = 'points = '

#with open(input_path, "r") as f:
#    with open(output_path, "w") as g:
#        for line in input_path:
#            Data = f.readline()
#            Data = str(Data)
#            print Data
#            post_d1 = Data.partition(d1)[2]
#            g.write(post_d1)
			
import json
import csv

f = open(input_path)
data = json.load(f)
f.close()

f=csv.writer(open(output_path,'wb+'))

for item in data:
  f.writerow([item['pk'], item['model']] + item['fields'].values())
