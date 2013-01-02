# Assumes x-coordinate grow from left to right, y from top to bottom, this is what the SVG people chose
import sys
if len(sys.argv) < 5:
    print "%s file xmin xmax ymin ymax"%(sys.argv[0])
    sys.exit(1)
points = map(lambda x: map(float, x.strip().split(',')) ,open(sys.argv[1]).readlines())
points = sorted(map(lambda p: (p[0], -p[1]), points))
xmin = float(sys.argv[2])
xmax = float(sys.argv[3])
ymin = float(sys.argv[4])
ymax = float(sys.argv[5])
yorigin = points[0][1]
xorigin = points[0][0]
xtranslate = (xmax - xmin) / (points[-1][0] - xorigin)
ytranslate = (ymax - ymin) / (points[-1][1] - yorigin)
for point in points:
    print "%f,%f"%((point[0] - xorigin) * xtranslate + xmin, (point[1] - yorigin) * ytranslate + ymin)
