#!/usr/bin/python

from sys import stdin,stdout

while True:
	
	line =stdin.readline().strip() #remove enter
	if len(line) ==0 :
		break#exit the while loop
	words=line.split()
	
	for number in range(len(words)-1):
		stdout.write( words[number]+"\t"+words[number+1]+"\t1\n")


