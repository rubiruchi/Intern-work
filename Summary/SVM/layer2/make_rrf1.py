import pandas as pd
import numpy as np
import sys

Name = sys.argv[1]
log = open(Name,"r")
makefile = open("rrf1-"+Name,"w")
number = 0
TN = 0
TP = 0
FN = 0
FT = 0
r = 0
t1 = 0
t2 = 0
t3 = 0
makefile.write("Gamma,Coef0,Degree,Recall,Precision,F1-score\n")
for i in log:

    if number == 0 and i[0] == "k":
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
        g = i.replace("  "," ").replace("   "," ").replace("[  ","[").replace("[ ","[")
        temp = g.split(" ")
        print temp
        TN = float(temp[2].replace("[[",""))
        FP = float(temp[3].replace("]",""))
        number += 1
    elif number == 2:
        g = i.replace("  "," ").replace("   "," ").replace("[  ","[").replace("[ ","[")
        temp = g.split(" ")
        FN = float(temp[1].replace("[",""))
        if temp[2] != '':
             TP = float(temp[2].replace("]]",""))
        else:
            TP = float(temp[3].replace("]]",""))
        recall = TP/(TP+FN)
        precision = TP/(TP+FP)
        temp1 = 2*recall*precision
        temp2 = recall+precision
        f1_score = temp1/temp2
        f1_score = float("{0:.2f}".format(f1_score))
        recall = float("{0:.2f}".format(recall))
        precision = float("{0:.2f}".format(precision))
        t1 += recall
        t2 += precision
        t3 += f1_score
        number += 1
        r  += 1
    elif number == 3 and i == "--\n":
        number  = 1

    if r == 10:
        makefile.write(str(t1/10)+","+str(t2/10)+","+str(t3/10)+"\n")
        t1 = 0
        t2 = 0
        t3 = 0
        number = 0
        r =0
makefile.close()
