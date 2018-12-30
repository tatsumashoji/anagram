# -*- coding: utf-8 -*-
import sys,argparse
import itertools
from nltk.corpus import words

#-------------------------------------------------------------------------------------
#functions etc.
#-------------------------------------------------------------------------------------
#word database
wdic=words.words()
#permutation, combination function
def wp(w):
	return list(set(["".join(p) for p in itertools.permutations(w)]))
def wcn(w,n):
	return ["".join(p) for p in itertools.combinations(w,n)]
#return anagrams
def ang(w):
	pli=wp(w)
	out=[]
	for i in pli:
		if i in wdic:
			out.append(i)
	return out
#return anagrams under the specified length
def angg(w,nl):
	target=[]
	for i in nl:
		target+=wcn(w,i)
	out=[]
	for i in target:
		out+=ang(i)
	print "\t".join(sorted(list(set(out))))


#-------------------------------------------------------------------------------------
#main
#-------------------------------------------------------------------------------------
parser = argparse.ArgumentParser(description='')
parser.add_argument('-w', '--word', dest='word', required=True, help='')
parser.add_argument('-s', '--shortest', dest='shortest', required=True, help='')
parser.add_argument('-l', '--longest', dest='longest', required=True, help='')
args = parser.parse_args()
word=args.word
shortest=int(args.shortest)
longest=int(args.longest)

angg(word,range(shortest, longest+1))

sys.exit()