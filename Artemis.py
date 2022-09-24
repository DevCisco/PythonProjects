#lettura e scrittura di file testuale
fileobject=open("text.txt","w")
fileobject.write("First Astronaut to Moon\n")
fileobject.write("Neil A.\n")
fileobject.close()
fileobject=open("text.txt")
textLine=fileobject.readlines()
for line in textLine:
    print(line)
