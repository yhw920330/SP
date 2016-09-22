#!/usr/bin/python
from sys import stdin,stdout

Bigrams={}

while True:
	line=stdin.readline().strip()
	if line =="":
		break

	word_cnt=line.split('\t')
	word1=word_cnt[0] #store the first word
	word2=word_cnt[1] #store the second word
	cnt = word_cnt[2] #store the number of the pair
	bigramword =word1+" "+word2 #make two word as a key
	if bigramword in Bigrams: 
		Bigrams[bigramword] += 1
			
	else:
		Bigrams[bigramword]  = 1
	

#print the result
for word in Bigrams:
	stdout.write(word+"\t"+str(Bigrams[word])+"\n")

