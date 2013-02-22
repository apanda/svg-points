import sys
if len(sys.argv) < 2:
    print "Usage %s svg_file"%(sys.argv[0])
    sys.exit(1)
from xml.dom.minidom import parse
svg = parse(sys.argv[1])
paths = svg.getElementsByTagName('path')
import re
regex = """[MZLHVCSQTARmzlhvcsqtar][\d\,\.-]+"""
regex_numbers = """-?[\d\.]+"""
for path in paths:
    commands = re.findall(regex, str(path.getAttribute('d')))
    locationx = 0.0
    locationy = 0.0
    locations = []
    cubic_prev_control = None
    for command in commands:
        if command[0] is 'M':
            parts = re.findall(regex_numbers, command[1:])
            assert(len(parts) == 2)
            locationx = float(parts[0])
            locationy = float(parts[1])
            locations.append((locationx, locationy))
        elif command[0] is 'Z':
            continue
        elif command[0] is 'L':
            parts = re.findall(regex_numbers, command[1:])
            assert(len(parts) == 2)
            locationx = float(parts[0])
            locationy = float(parts[1]) 
            locations.append((locationx, locationy))
        elif command[0] is 'H':
            part = float(command[1:])
            locationx = part
            locations.append((locationx, locationy))
        elif command[0] is 'V':
            part = float(command[1:])
            locationy = part
            locations.append((locationx, locationy))
        elif command[0] is 'C':
            parts = re.findall(regex_numbers, command[1:])
            assert(len(parts) == 6)
            parts = map(float, parts)
            cubic_prev_control = (parts[2], parts[3])
            midx = (0.5 ** 3) * locationx + 3.0 * (0.5 ** 3) * parts[0] + 3.0 * (0.5 ** 3) * parts[2] + (0.5 ** 3) * parts[4]
            midy = (0.5 ** 3) * locationy + 3.0 * (0.5 ** 3) * parts[1] + 3.0 * (0.5 ** 3) * parts[3] + (0.5 ** 3) * parts[5]
            locations.append((midx, midy))
            locationx = parts[4]
            locationy = parts[5]
            locations.append((parts[4], parts[5]))
        elif command[0] is 'S':
            parts = re.findall(regex_numbers, command[1:])
            assert(len(parts) == 4)
            parts = map(float, parts)
            if cubic_prev_control is None:
                cubic_prev_control = (locationx, locationy)
            cp2 = (parts[0], parts[1])
            cp1 = (2 * locationx - cubic_prev_control[0], 2 * locationy - cubic_prev_control[1])
            cubic_prev_control = cp2
            ep = (parts[2], parts[3])
            parts = map(float, parts)
            midx = (0.5 ** 3) * locationx + 3.0 * (0.5 ** 3) * cp1[0] + 3.0 * (0.5 ** 3) * cp2[0] + (0.5 ** 3) * ep[0]
            midy = (0.5 ** 3) * locationy + 3.0 * (0.5 ** 3) * cp1[1] + 3.0 * (0.5 ** 3) * cp2[1] + (0.5 ** 3) * ep[1]
            locations.append((midx, midy))
            locationx = ep[0]
            locationy = ep[1]
            locations.append((locationx, locationy))
        elif command[0] is 'Q' or command[0] is 'T' or command[0] is 'A' or command[0] is 'R':
            raise Exception("Don't know how to interpret")
        elif command[0] is 'm':
            parts = re.findall(regex_numbers, command[1:])
            assert(len(parts) == 2)
            locationx += float(parts[0])
            locationy += float(parts[1])
            locations.append((locationx, locationy))
        elif command[0] is 'z':
            continue
        elif command[0] is 'l':
            parts = re.findall(regex_numbers, command[1:])
            assert(len(parts) == 2)
            locationx += float(parts[0])
            locationy += float(parts[1]) 
            locations.append((locationx, locationy))
        elif command[0] is 'h':
            part = float(command[1:])
            locationx += part
            locations.append((locationx, locationy))
        elif command[0] is 'v':
            part = float(command[1:])
            locationy += part
            locations.append((locationx, locationy))
        elif command[0] is 'c':
            parts = re.findall(regex_numbers, command[1:])
            assert(len(parts) == 6)
            parts = map(float, parts)
            cubic_prev_control = (parts[2] + locationx, parts[3] + locationy)
            midx = (0.5 ** 3) * locationx + 3.0 * (0.5 ** 3) * (locationx + parts[0]) + 3.0 * (0.5 ** 3) * (locationx + parts[2]) + (0.5 ** 3) * (locationx + parts[4])
            midy = (0.5 ** 3) * locationy + 3.0 * (0.5 ** 3) * (locationy + parts[1]) + 3.0 * (0.5 ** 3) * (locationy + parts[3]) + (0.5 ** 3) * (locationy + parts[5])
            locationx += parts[4]
            locationy += parts[5]
            locations.append((midx, midy))
            locations.append((locationx, locationy))
        elif command[0] is 's':
            parts = re.findall(regex_numbers, command[1:])
            assert(len(parts) == 4)
            parts = map(float, parts)
            cp2 = (locationx + parts[0], locationy + parts[1])
            if cubic_prev_control is None:
                cubic_prev_control = (locationx, locationy)
            cp1 = (2 * locationx - cubic_prev_control[0], 2 * locationy - cubic_prev_control[1])
            cubic_prev_control = cp2
            ep = (locationx + parts[2], locationy + parts[3])
            parts = map(float, parts)
            midx = (0.5 ** 3) * locationx + 3.0 * (0.5 ** 3) * cp1[0] + 3.0 * (0.5 ** 3) * cp2[0] + (0.5 ** 3) * ep[0]
            midy = (0.5 ** 3) * locationy + 3.0 * (0.5 ** 3) * cp1[1] + 3.0 * (0.5 ** 3) * cp2[1] + (0.5 ** 3) * ep[1]
            locations.append((midx, midy))
            locationx = ep[0]
            locationy = ep[1]
            locations.append((locationx, locationy))
        elif command[0] is 'q' or command[0] is 't' or command[0] is 'a' or command[0] is 'r':
            print command[0]
            raise Exception("Don't know how to interpret")
        else:
            raise Exception("Don't like this input")
        if command[0] not in ['C', 'c', 's','S']:
            cubic_prev_control = None
for location in locations:
    print str.format("{0},{1}", location[0], location[1])
polylines = svg.getElementsByTagName('polyline')
points = paths[0].getAttribute('points')
points = points.split()
points = map(lambda p: tuple(map(float, p.split(','))), points)
for point in points:
  print str.format("{0},{1}", point[0], point[1]) 
