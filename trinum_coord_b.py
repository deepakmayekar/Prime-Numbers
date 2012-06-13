# this small python program makes a textfile that prints out
# prime numbers in rows of increasing size.  the size of
# each row increases with size being the next prime number
# i created this program to see if I see patterns when printing
# prime numbers this way
# this is based on trinum.py but will output coordinates for 
# graphing (such as in R)

SIZE = 510510

#First, read in the primes
p = []
f = open("p%d.txt" %SIZE) #this file is generated by sieve.py
for line in f:
    p.append(int(line))

#Next, print out primes rows

cc = 0 # column count
lc = 0 # line count

outfile = open('ptcb%d.txt' %SIZE, 'w')
    
for i in range(2,SIZE):
    if i in p:
        outfile.write("%d,%d,%d\n" %(i, cc, lc))
    else:
        pass
        
    cc += 1
    if cc >= lc:
        lc += 1
        cc = 0
        #print
        #outfile.write('\n')
    else:
        pass
        
outfile.close()
    
