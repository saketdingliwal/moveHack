import fileinput
import sys

with fileinput.FileInput(sys.argv[1], inplace=False, backup='.bak') as file:
	for line in file:
		# print("aaya")
		ok = line.replace('}} , {', '}} , \n{')
		print(ok.replace('][ ', ' , \n'))