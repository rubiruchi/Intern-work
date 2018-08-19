import pandas as pd
import numpy as np
import sys

Name = sys.argv[1]
log = open(Name,"r")
makefile = open("t-"+Name,"w")
number = 0
makefile.write("Gamma,Coef0,Degree,Train,Test\n")
for i in log:
    if number == 0:
        if i[1:3] == str(10) and i[3:5] == str(10):
            makefile.write(str(i[1:3])+","+str(i[3:5])+","+str(i[5])+",")
        elif i[1:3] == str(10):
            makefile.write(str(i[1:3])+","+str(i[3])+","+str(i[4])+",")
        elif i[2:4] == str(10):
            makefile.write(str(i[1])+","+str(i[2:4])+","+str(i[4])+",")
        else:
            makefile.write(str(i[1])+","+str(i[2])+","+str(i[3])+",")
        number += 1
    elif number == 1:
        t2 = float(i)/10.0
        t2 = float("{0:.2f}".format(t2))
        makefile.write(str(t2)+",")
        number += 1
    elif number == 2:
        t2 = float(i)/10.0
        t2 = float("{0:.2f}".format(t2))
        makefile.write(str(t2)+"\n")
        number = 0
makefile.close()
