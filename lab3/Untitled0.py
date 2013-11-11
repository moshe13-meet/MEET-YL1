# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import csv
f = open('cig.csv', 'rb')
reader = csv.reader(f)

for row in reader :
    a=row[0].replace("\t"," ")
    a=a.split()
    c=[a[0]]
    b=a[1:]
    b=map(float,b)
    c.extend(b)
    print c

f.close()

# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


