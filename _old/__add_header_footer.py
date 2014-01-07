INPUT_FILE = '102_(LOOPS)/27.sbp'
OUTPUT_FILE = ''.join(INPUT_FILE.split('.')[:-1]) + '_with_header_footer.sbp'
Z_OFFSET = 0.5

with open(INPUT_FILE, 'r') as f:
    data = []
    for line in f:
        data.append([float(x.strip()) for x in line.strip().split(',')[1:]])

with open(OUTPUT_FILE, 'w') as f:
    # header
    f.write('# add Move Speed, XY-speed = 0.5 in/sec, Z-speed = 0.5 in/sec\n')
    f.write('MS, 0.5, 0.5\n')
    f.write('# add Jog to (0,0)\n')
    f.write('J2, 0, 0\n')
    f.write('# add Jog to (above the first point (nextline\'s_X-value, nextline\'s_Y-value, Z-variable))\n')
    first = data[0]
    f.write('J3, ' + str(first[0]) + ', ' + str(first[1]) + ', ' + str(first[2]+Z_OFFSET) + '\n')
    # main content
    for element in data:
        f.write('M3, '  + str(element[0]) + ', ' + str(element[1]) + ', ' + str(element[2]) + '\n')
    # footer
    f.write('# add Jog to (above the first point (nextline\'s_X-value, nextline\'s_Y-value, Z-variable))\n')
    f.write('J3, ' + str(first[0]) + ', ' + str(first[1]) + ', ' + str(first[2]+Z_OFFSET) + '\n')
    f.write('# add Jog to (0,0)\n')
    f.write('J2, 0, 0\n')

