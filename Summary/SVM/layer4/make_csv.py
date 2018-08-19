import pandas as pd
import numpy as np
import sys

Name = sys.argv[1]
log = open(Name,"r")
makefile = open("n-"+Name,"w")
number = 0
makefile.write("Gamma,Coef0,Degree\n")
for i in log:
    if number == 0:
        if i[5:7] == str(10) and i[7:9] == str(10):
            makefile.write(str(i[5:7])+","+str(i[7:9])+","+str(i[9])+",")
        elif i[5:7] == str(10):
            makefile.write(str(i[5:7])+","+str(i[7])+","+str(i[8])+",")
        elif i[6:8] == str(10):
            makefile.write(str(i[5])+","+str(i[6:8])+","+str(i[8])+",")
        else:
            makefile.write(str(i[5])+","+str(i[6])+","+str(i[7])+",")
        number += 1
    elif number == 1:
        temp = i.split(" ")
        t2 = float(temp[0].replace(")","").replace("%","")) + float(temp[2].replace(")","").replace("%",""))
        t2 = float("{0:.2f}".format(t2))
        t3 = float(temp[0].replace(")","").replace("%","")) - float(temp[2].replace(")","").replace("%",""))
        t3 = float("{0:.2f}".format(t3))
        makefile.write(str(temp[0].replace(")","").replace("%",""))+","+str(t2)+","+str(t3)+"\n")
        number += 1
    elif number == 2:
        number = 0
makefile.close()
