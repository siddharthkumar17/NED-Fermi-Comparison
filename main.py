__author__ = 'Siddharth Kumar'

import sys
import FermiLATGRBXMLTools

f = open('NED_TABLE.txt','r')

print(f.readline())
print(f.readline())

#for line in f:
    #print(line, end='')

xml = FermiLATGRBXMLTools.xml('FERMI_TABLE.xml')

xml.xml2txt()
GRBs = xml.ExtractGRBs()

for name in xml.ExtractData()['GRBNAME']:
    GRB = GRBs[name]
    print(GRB.RA)