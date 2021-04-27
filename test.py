testdnamelist=[]
f = open("test.txt")
for line in f:
    line = line.strip()
    testdnamelist.append(line)
f2 = open("result.txt","w")
for item in testdnamelist:
    if(len(item)<24):
        f2.write(item.strip()+",notdga\n")
    else:
        f2.write(item.strip()+",dga\n")
f.close()
f2.close()