import csv
import sys

divt = {}
areas = {}
with open(sys.argv[1]) as f:
	ok = csv.reader(f, delimiter=',')
	for r in ok:
		print(r[6], r[3], r[4])
		print(r[6][:10]+' '+r[6][11:13])
		areas[r[3]] = '1'
		divt[r[0]] = '1'

print( len(divt), len(areas) )