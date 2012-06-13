#public domain
#This file will generate a list of numbers which have about the same
#density as the prime numbers, but based on random.random() function 

import math
import random

SIZE = 510510

outfile = open('pr%d.txt' %SIZE, 'w')
    
for i in range(2,SIZE):
    ran = random.random()
    prob = 1.0 / math.log(i)
    if ran < prob:
        outfile.write("%d\n" %i)
    else:
        pass
        
outfile.close()
    
