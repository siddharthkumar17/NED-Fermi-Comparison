__author__ = 'Siddharth Kumar'

import sys
import re

import xml.etree.ElementTree as ET

tree = ET.parse('FERMI_TABLE.xml')
f = open('NED_TABLE.txt','r')

print(f.readline())

root = tree.getroot()

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

for line in f:
    re.sub(' +',' ',line)
    RA = re.sub('h|m|s',' ',line.split()[3])
    DEC = re.sub('d|m|s',' ',line.split()[4])
    NAME = line.split()[2]
    NEDList.append(GRB(NAME,HMS2deg(RA,DEC)[0],HMS2deg(RA,DEC)[1]))



for GRBs in root.findall('GRB'):
    RA = GRBs.find('RA').text
    DEC = GRBs.find('DEC').text
    NAME = GRBs.find('GRBNAME').text
    FermiList.append(GRB(NAME,RA,DEC))

for NED in NEDList:
    for Fermi in FermiList:

        if(abs(NED.RA-Fermi.RA)<=1 and abs(NED.DEC-Fermi.DEC)<1):
            print(NED.NAME,' = ',Fermi.NAME)