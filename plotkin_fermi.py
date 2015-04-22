__author__ = 'Siddharth Kumar'
__author__ = 'Siddharth Kumar'

import re
import math

class GRB:

    def __init__(self,name,ra,dec):

        self.NAME = str(name)
        self.RA = float(ra)
        self.DEC = float(dec)


        #self.NAME = str(name)+' ('+str(self.RA)+','+str(self.DEC)+')' for debug

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

fermi = open('FERMI_TABLE.txt','r')
t3 = open('NED_TABLE.txt','r')

t3.readline()

range = 1

t3list = []

FermiList = []

for line in t3:

    line=re.sub(' +',' ',line)

    RA = re.sub('h|m|s',' ',line.split()[3])
    DEC = re.sub('d|m|s',' ',line.split()[4])
    NAME = line.split()[2]

    t3list.append(GRB(NAME,HMS2deg(RA,DEC)[0],HMS2deg(RA,DEC)[1]))

for line in fermi:

    line = re.sub(' +',' ',line)
    line = re.sub(',',' ',line)
    line = re.sub('\)',' ',line)
    line = re.sub('}',' ',line)

    RA=line.split()[0]
    DEC = line.split()[1]
    NAME = line.split()[2]

    FermiList.append(GRB(NAME,RA,DEC))

results=0

print('FERMI OBJECT -> T3 OBJECT')
for t3obj in t3list:
    while len(t3obj.NAME)<19:
                t3obj.NAME+=' '

list3 = []
for Fermi in FermiList:

    list = []
    list2=[]

    for t3obj in t3list:
        list.append(((t3obj.RA-Fermi.RA)**2+((t3obj.DEC-Fermi.DEC)*math.cos(math.radians(t3obj.DEC-Fermi.DEC)))**2)**.5)

    print(Fermi.NAME,'-> ',end='')


    b = False

    for l in list:

        if l <= 1 and b:
            print(',',t3list[list.index(l)].NAME,'AT DIST =',l,end=', ')
            list2.append(t3list[list.index(l)].NAME)

        if l <= 1:
            print(t3list[list.index(l)].NAME,'AT DIST =',l,end='')
            results+=1
            b=True
            list2.append(t3list[list.index(l)].NAME)

    if b == False:
        print('NO RESULTS WITHIN RANGE OF',range,'-> CLOSEST = ',t3list[list.index(min(list))].NAME,'AT DIST =',min(list))
    else:
        print('')

    if len(list2)>1:
        s=Fermi.NAME+' HAS '+str(len(list2))+' RESULTS -> '
        for q in list2:
            s+=q+', '
        s=s[:-2]
        list3.append(s)

print('---------------------------------------------------------------------------')

print(results,'HAVE RESULTS WITHIN RANGE OF',range,'DEGREE',end='')

if range>1:
    print('s')
else:
    print('')

print('---------------------------------------------------------------------------')

for r in list3:
    print(r)
