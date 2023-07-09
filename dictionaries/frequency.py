# =====================

import sys
sys.path.append('/Users/nicolas/Desktop/NaturaLingua/utils')
from utils import save_object, get_object, getListFiles, createNecessaryFolders

def orderByKey(unsorted_dict):
	sorted_dict = sorted(unsorted_dict.items())
	return sorted_dict

def orderByValue(dict):
	step1=sorted(dict.items(), key=lambda item: item[1], reverse=True)
	return step1


# ----------------------
# suite de 1,2,3,4,5 mots

def getLines(listeFiles):
	lines2=[]
	for fileName in listeFiles:
		with open(fileName, "r") as f:
			lines = f.readlines()
			for line in lines:
				if(len(line)<2):
					continue
				if(line[0:2] != '- '):
					continue
				index=line.find('[')
				if(index == -1):
					lines2.append(line[2:].lower().strip())
				else:
					lines2.append(line[2:index].lower().strip())
	return lines2

def isLimit(c):
	liste=['-', '.','?','!',':',';',',',
	'\\','[',']','{','}','&', '<', '>', '=', '#',
	'。','،','؟','！','，']
	# '(',')',
	return c in liste

# lines2=getLines(listeFiles)
def getPhrases(lines2):
	aaa=0
	# listePhrases=[['une','super','phrase'],['une','super','phrase']]
	listePhrases=[]
	for line in lines2:
		aaa+=1
		print(aaa)
		s=''
		i=0
		lvl=0
		while i < len(line):
			c=line[i]
			if(not isLimit(c)):
				if(c=='('):
					lvl+=1
				elif(c==')'):
					lvl-=1
				elif(lvl==0):
					s+=c
			if(isLimit(c) or i==(len(line)-1)):
				listePhrases.append(s.split())
				s=''
			i+=1
	return listePhrases

def buildKey(suiteMots):
	s=''
	if(len(suiteMots)==0):
		return ''
	for i in range(len(suiteMots)-1):
		mot=suiteMots[i]
		s+=mot+' '
	s+=suiteMots[-1]
	return s

def ajouteKey(dico, key):
	if not (key in dico):
		dico[key]=1
	else:
		dico[key]+=1


# lines2=getLines(listeFiles)
def getFrequencies(lines2, fileNamePkl, lastIndex=16000):
	listePhrases=getPhrases(lines2)
	bigDictionary={}
	longueur=len(listePhrases)
	for a in [1,2,3,4,5]:
		i=0
		for phrase in listePhrases:
			nb=len(phrase)
			for b in range(nb-a, -1, -1):
				key=buildKey(phrase[b:(b+a)])
				ajouteKey(bigDictionary, key)
			i+=1
			print(f'\r{i/longueur*100} %', end='', flush=True)
	answer=orderByValue(bigDictionary)
	save_object(answer[:lastIndex], fileNamePkl)


def prettyPrint(fileNamePkl, outputFileName1, outputFileName2, lastIndex=8000):
	answer = get_object(fileNamePkl)
	file=open(outputFileName1,'w+')
	for index, (a, b) in enumerate(answer):
		if(index > lastIndex):
			break
		ooo=file.write(f'• {a} ({b})\n')
	file.close()
	file2=open(outputFileName2,'w+')
	for index, (a, b) in enumerate(answer):
		if(index > lastIndex):
			break
		ooo=file2.write(f'{a}={b}\n')
	file2.close()


import glob
import os.path
import os


def getOutputFileNames(language):
	parent2=f'/Users/nicolas/Desktop/NaturaLingua/dictionaries_results/{language}'
	fileNamePkl=f'{parent2}/freq.pkl'
	outputFileName1=f'{parent2}/freqPrint.txt'
	outputFileName2=f'{parent2}/freqAnki.txt'
	return fileNamePkl, outputFileName1, outputFileName2

def getFrequenciesLanguage(language):
	language = language.capitalize()
	parent = '/Users/nicolas/Desktop/NaturaLingua/SubsToBilingualText'
	patterns=[f'{parent}/youtube/{language}/**.txt', f'{parent}/movies/{language}/**.txt']
	listeFiles = getListFiles(patterns)
	fileNamePkl, outputFileName1, outputFileName2 = getOutputFileNames(language)
	createNecessaryFolders(fileNamePkl)
	lines2=getLines(listeFiles)
	getFrequencies(lines2, fileNamePkl)
	prettyPrint(fileNamePkl, outputFileName1, outputFileName2)


# getFrequenciesLanguage('russian')




