#! /usr/bin/env python
import os
import sys

outaver = "orbitapromedio.dat"
bpmf="../somebpm.madx"
pfav = open(outaver,'w')
pfbpm =open(bpmf,'r')
ind = 0
for line in pfbpm:
    ind = ind +1 
    sline = line.split("\"")
    print  sline[1]
    cmdsystem =  "./readtrackone1.py " + "1 " + "1" + " 183 "+ "1 " +sline[1]
    print cmdsystem
    os.system(cmdsystem)
    cmdsystem = "cp elipse.dat elipse" + sline[1]+".dat"
    print cmdsystem
    os.system(cmdsystem)
    felip="elipse" + sline[1]+".dat"
    fp = open(felip,'r')
    xaver = 0
    n = 0
    for linee in fp:
        n = n + 1
        slinee=linee.split(None)
        xaver = xaver + float(slinee[0])
    xaver = xaver/n
    print >> pfav, slinee[2], xaver





