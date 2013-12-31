fIn = open(r"002_(POINTS).csv")  # use raw strings for windows file names
fOut = open(r"100_(POINTS).csv", "w")
for line in fIn:
    fOut.write(line)
fIn.close()
fOut.close()