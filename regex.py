# can be used for smart searching or extraction
#  a structured way to search for information

import re
line = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2023"
y = re.findall('^From .*@([^ ]*)', line)
print(y)

hand = open('assets/mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))