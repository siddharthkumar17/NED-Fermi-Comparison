__author__ = 'Siddharth Kumar'

import sys
import re

import xml.etree.ElementTree as ET

fermi = open('FERMI_TABLE.txt','r')
ned = open('NED_TABLE.txt','r')

ned.readline()



class GRB:
    def __init__(self,name,ra,dec):
        self.NAME = str(name)
        self.RA = float(ra)
        self.DEC = float(dec)


def HMS2deg(ra='', dec=''):
  RA, DEC, rs, ds = '', '', 1, 1
  if dec:
    D, M, S = [float(i) for i in dec.split()]
    if str(D)[0] == '-':
      ds, D = -1, abs(D)
    deg = D + (M/60) + (S/3600)
    DEC = '{0}'.format(deg*ds)

  if ra:
    H, M, S = [float(i) for i in ra.split()]
    if str(H)[0] == '-':
      rs, H = -1, abs(H)
    deg = (H*15) + (M/4) + (S/240)
    RA = '{0}'.format(deg*rs)

  if ra and dec:
    return [RA, DEC]
  else:
    return RA or DEC


NEDList = []
FermiList = []

for line in ned:
    line=re.sub(' +',' ',line)
    RA = re.sub('h|m|s',' ',line.split()[3])
    DEC = re.sub('d|m|s',' ',line.split()[4])
    NAME = line.split()[2]
    NEDList.append(GRB(NAME,HMS2deg(RA,DEC)[0],HMS2deg(RA,DEC)[1]))



for line in fermi:
    line = re.sub(' +',' ',line)
    line = re.sub(',',' ',line)
    line = re.sub('\)',' ',line)
    line = re.sub('}',' ',line)
    RA=line.split()[0]
    DEC = line.split()[1]
    NAME = line.split()[2]
    FermiList.append(GRB(NAME,RA,DEC))

print(len(FermiList))
list = []
for NED in NEDList:
    dist = ((NED.RA-FermiList[0].RA)**2+(NED.DEC-FermiList[0].DEC)**2)**.5
    for Fermi in FermiList:
        list.append(((NED.RA-Fermi.RA)**2+(NED.DEC-Fermi.DEC)**2)**.5)
    print(NED.NAME,' = ')#FermiList[list.index(min(list))].NAME)

