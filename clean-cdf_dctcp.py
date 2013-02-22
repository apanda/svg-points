import sys
cdf = open(sys.argv[1])
avg = 0.0
for l in cdf:
    if ',' not in l:
        continue
    p = map(float, l.split(','))
    print "%f,%f"%(p[0]*1460, p[1])
    avg += p[0]*1460.0*p[1]
print >>sys.stderr, (avg / 1460.0) *1500

