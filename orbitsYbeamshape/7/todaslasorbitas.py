#! /usr/bin/env python
import os
import sys
output="todaslasorbitas.gplot"
pf = open(output,'w')
#inicial = "  gnuplot -p -e \"p  "
graphtype = "set term postscript eps\n"
pf.write(graphtype)
graphname = "set output \"plot.eps\"\n"
pf.write(graphname)
inicial = " p "
#print >>pf, inicial
pf.write(inicial)
for i in range(1,183):
    cmdsystem = "./readtrackone1.py " + "1 " + "1" + " 183 "+ str(i)+ " BPM.29R1.B1"
    print cmdsystem
    os.system(cmdsystem)
    cmdsystem = "cp orbita.dat orbita" + str(i)+".dat"
    print cmdsystem
    os.system(cmdsystem)
    cmdsystem = "\'./orbita"+str(i)+".dat\' u 1:2 w l notitle, "
    #print >> pf, cmdsystem
    pf.write(cmdsystem)
cmdsystem = "./readtrackone1.py " + "1 " + "1" + " 183 "+ str(i)+ " BPM.29R1.B1"
print cmdsystem
os.system(cmdsystem)
cmdsystem = "cp orbita.dat orbita" + str(i+1)+".dat"
print cmdsystem
os.system(cmdsystem)
cmdsystem = "\'./orbita"+str(i+1)+".dat\' u 1:2 w l notitle  "
#print >> pf, cmdsystem
pf.write(cmdsystem)
