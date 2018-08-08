import csv
import sys
import numpy as np
import pprint

def get_time(date_str):
	date = int(date_str[8:10])
	time = int(int(date_str[11:13])/2)

	return date, time

areas = {}
iterr = 0

head = 0
with open(sys.argv[1]) as f:
	ok = csv.reader(f, delimiter=',')
	for r in ok:
		if(head==0):
			head+=1
			continue
		if not (r[3] in areas):
			areas[r[3]] = iterr
			iterr += 1

date = {}

fnl_matr = np.zeros((len(areas), 12), dtype='int64')

head = 0
with open(sys.argv[1]) as f:
	ok = csv.reader(f, delimiter=',')
	for r in ok:
		if(head==0):
			head+=1
			continue
		dt, tm = get_time(r[6])
		date[dt] = 1
		fnl_matr[areas[r[3]]][tm] += 1

print(date)

print(fnl_matr)
