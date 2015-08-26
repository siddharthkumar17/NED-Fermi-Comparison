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
t6 = open('t6.txt','r')


range = 1

t6list = []

FermiList = []
for line in t6:

    line=re.sub(' +',' ',line)

    RA = line.split()[1]
    DEC = line.split()[2]
    NAME = 'J'+line.split()[0]

    t6list.append(GRB(NAME,RA,DEC))

for line in fermi:

    line = re.sub(' +',' ',line)
    line = re.sub(',',' ',line)
    line = re.sub('\)',' ',line)
    line = re.sub('}',' ',line)

    RA=line.split()[0]
    DEC = line.split()[1]
    NAME = line.split()[2]

    FermiList.append(GRB(NAME,RA,DEC))

print('T5 OBJECT -> FERMI OBJECT')

list3 = []
list4 = []

for T5 in t6list:

    list = []

    listTemp = []

    for Fermi in FermiList:
        list.append(((T5.RA-Fermi.RA)**2+(T5.DEC-Fermi.DEC)**2)**.5)




    b = False
    listTemp=list
    listTemp.sort()


    if listTemp[0] <= 1:
            #print(FermiList[list.index(listTemp[0])].NAME,'AT DIST =',listTemp[0])

            b=True
            list4.append('TRUE')




    else:
        #print('NO RESULTS WITHIN RANGE OF',range,'-> CLOSEST = ',FermiList[list.index(listTemp[0])].NAME,'AT DIST =',listTemp[0])
        list4.append('FALSE')




print('---------------------------------------------------------------------------')



for a in list4:
    print(a)

print(len(list4))