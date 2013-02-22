import sys
if len(sys.argv) < 2:
    print "Usage %s svg_file"%(sys.argv[0])
    sys.exit(1)
from xml.dom.minidom import parse
svg = parse(sys.argv[1])
polylines = svg.getElementsByTagName('polyline')
import re
points = paths[0].getAttribute('points')
points = points.split()
points = map(lambda p: tuple(map(float, p.split(','))), points)
for point in points:
  print str.format("{0},{1}", point[0], point[1]) 
