

import sys
sys.path.append('/Users/nicolas/Desktop/NaturaLingua/utils')
from utils import save_object, get_object

# deprecated
def getMots_old(txt):
	mots=txt.split(' ')
	for i in range(len(mots)):
		mots[i]=mots[i].lower()
		for a in ['.',',','!','?',';',':','。','،','؟','！','，','\u202f', '\xa0']:
			mots[i]=mots[i].replace(a, '')
	return mots

import re
def getMots(txt):
	mots = re.findall(r"[\w']+",txt)
	for i in range(len(mots)):
		mots[i]=mots[i].lower()
	return mots

def isIn(expr, phrase):
	if(f' {expr} ' in phrase):
		return True
	else:
		index = phrase.find(expr)
		if(index == -1):
			return False
		l = len(expr)
		limits = [' ',',','.','!',':',';','?','"']
		requirement1 = (index + l >= len(phrase) or (phrase[index + l] in limits))
		requirement2 = (index == 0) or (phrase[index - 1] in limits)
		return (requirement1 and requirement2)


class Word:
	def __init__(self, romanized, count, rank=-1, meaning='', original=''):
		self.romanized = romanized
		self.count = count
		self.original = original
		self.rank = rank
		self.meaning = meaning
		self.len = -1
	def __str__(self) -> str:
		if self.original == '' or self.original=='b':
			debut = self.romanized
		else:
			debut = f'{self.original} ({self.romanized})'
		return (f'{debut} [rk={self.rank}] : {self.meaning}')
	def str2(self) -> str:
		if self.original == '':
			debut = self.romanized
		else:
			debut = f'{self.original} ({self.romanized})'
		return (f'{debut} [ct={self.count}] : {self.meaning}')
	def computeLen(self):
		self.len = len(getMots(self.romanized))


def orderByValue_old(dict):
	step1=sorted(dict.items(), key=lambda item: item[1].count, reverse=True)
	result = list(map(lambda a: a[1], step1))
	return result

def getListeWords_old(language, fromEnglish):
	if(not fromEnglish):
		return get_object(f'/Users/nicolas/Desktop/NaturaLingua/dictionaries_results/{language}/meanings2.pkl')
	else:
		return get_object(f'/Users/nicolas/Desktop/NaturaLingua/dictionaries_results/english2{language}/meanings2.pkl')

def ajouterExpression(dico, mot, exp):
	if not (mot in dico):
		dico[mot] = [exp]
	else:
		dico[mot].append(exp)

import sys
sys.path.append('/Users/nicolas/Desktop/NaturaLingua/utils')
from utils import languagesLatines, languagesNonLatines, languages


def getDico123(wordsByFreq, listeWords):
	dico={}
	for index,word in enumerate(wordsByFreq):
		mots=getMots(word.romanized)
		if(len(mots) >= 3):
			n=len(mots)
			for i in range(2,n):
				for j in range(0, n-i+1):
					sub=' '.join(mots[j:j+i])
					if(sub in listeWords):
						ajouterExpression(dico,sub,(index, word.count))
	return dico

def getNewWordsByFreq(wordsByFreq, dico):
	newWordsByFreq=[]
	problematicWords=[]
	for word in wordsByFreq:
		txt=word.romanized
		if(not txt in dico):
			newWordsByFreq.append(word)
			continue
		mots=getMots(txt)
		count=word.count
		liste=dico[txt]
		foundProblem=False
		for surExp in liste:
			if surExp[1] >= count/1.15:
				foundProblem=True
		if(not foundProblem):
			newWordsByFreq.append(word)
		else:
			problematicWords.append(txt)
	return newWordsByFreq, problematicWords

def computeNewWordsByFreq(language, fromEnglish):
	print('computeNewWordsByFreq',language)
	listeWords=getListeWords_old(language, fromEnglish)
	wordsByFreq=orderByValue_old(listeWords)
	dico=getDico123(wordsByFreq, listeWords)
	newWordsByFreq, problematicWords = getNewWordsByFreq(wordsByFreq, dico)
	newWordByFreq2=[]
	for (index,word) in enumerate(newWordsByFreq):
		word2=Word(word.romanized, word.count, index, word.meaning, word.original)
		word2.computeLen()
		if(language in languagesLatines):
			if((word2.romanized == 'b' or word2.romanized == '')):
				word2.romanized=word2.original
			word2.original=''
		newWordByFreq2.append(word2)
	root='/Users/nicolas/Desktop/NaturaLingua/tatoeba/wordsByFreq'
	fileName=f'{root}/{language}.pkl'
	if(fromEnglish):
		fileName=f'{root}/english2{language}.pkl'
	save_object(newWordByFreq2, fileName)


def computeAllNewWordsByFreq():
	for language in languages :
		computeNewWordsByFreq(language)

# computeAllNewWordsByFreq()

def getWordsByFreq(language, fromEnglish):
	if (not fromEnglish):
		return get_object(f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/wordsByFreq/{language}.pkl')
	else:
		return get_object(f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/wordsByFreq/english2{language}.pkl')

def getSortedByFreq(words):
	return sorted(words, key=lambda item: item.rank)

def getSortedByAlpha(words):
	return sorted(words, key=lambda item: item.romanized)

def getListeWords(language, fromEnglish):
	wordsByFreq=getWordsByFreq(language, fromEnglish)
	dico={}
	for word in wordsByFreq:
		dico[word.romanized]=word
	return dico

# wordsByAlpha=getSortedByAlpha(wordsByFreq)

# for language in languages:
# 	wordsByFreq = getWordsByFreq(language)
# 	problems=0
# 	for word in wordsByFreq:
# 		if((word.original == 'b' or word.original == '') and (word.romanized == 'b' or word.romanized == '')):
# 			problems+=1
# 	print(language, problems)
# 	input('enter to continue...')



# -------------------------
# parse docs tatoeba


import sys
sys.path.append('/Users/nicolas/Desktop/NaturaLingua/SubsToBilingualText/transliterate')
from transliterateAll import transliterate, transliterate2, getCode
from transliterateList import transliterateList2

class PhraseTraduite:
	def __init__(self, original, translation, romanized='', rank=-1, unknownsNumber=0, id=-1):
		self.original = original
		self.translation = translation
		self.romanized = romanized
		self.rank = rank # argmax (ranks connus) _ should be low to high
		self.unknownsNumber = unknownsNumber
		self.id=id
		self.len=-1
	def __str__(self) -> str:
		return (f'{self.original} ({self.romanized}) : {self.translation}')
	def computeLen(self):
		self.len = len(getMots(self.romanized))


def savePhrases(phrases, language, fromEnglish):
	path='/Users/nicolas/Desktop/NaturaLingua/tatoeba/phrases'
	filename=f'{path}/{language}.pkl'
	if fromEnglish:
		filename=f'{path}/english2{language}.pkl'
	save_object(phrases, filename)

def getPhrases(language, fromEnglish=False, path='/Users/nicolas/Desktop/NaturaLingua/tatoeba/phrases'):
	filename=f'{path}/{language}.pkl'
	if(fromEnglish):
		filename=f'{path}/english2{language}.pkl'
	phrases = get_object(filename)
	return phrases

def getPhrasesHebrew():
	phrases_old = getPhrases('hebrew', path='/Users/nicolas/Desktop/NaturaLingua/tatoeba/big pkl files')
	phrases=[]
	for phrase_old in phrases_old:
		phrases.append(PhraseTraduite(phrase_old.original, phrase_old.translation, phrase_old.romanized))
	return phrases

def getPhrasesFromTsv(language):
	print('getPhrasesFromTsv', language)
	fileName=f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/tsv files/{language}.tsv'
	f=open(fileName, "r")
	lines = f.readlines()
	liste=[]
	longueur=len(lines)
	if(not (language in languagesLatines)):
		for index, line in enumerate(lines):
			print(f'\r{index/longueur*100} %', end='', flush=True)
			words=line.strip().split('\t')
			liste.append(PhraseTraduite(words[1], words[3]))
	else:
		for index, line in enumerate(lines):
			print(f'\r{index/longueur*100} %', end='', flush=True)
			words=line.strip().split('\t')
			liste.append(PhraseTraduite('', words[3], words[1]))
	return liste


# phrases=[PhraseTraduite('מה נשמע', 'how are you')]
# transliterateListHebrew(phrases)
# phrases[0].romanized


def stringWithoutStrangeUnicode(s):
	dico={'،':',', '。':'.', '،':',', '؟':'?', '！':'!','，':',', '\xa0':' ', '\u202f':' ', '\u202c':'', '\u202b':'', '\u200f':'','？':'?'}
	for key in dico:
		s=s.replace(key, dico[key])
	return s

def cleanup(phrases):
	for phrase in phrases:
		phrase.romanized = stringWithoutStrangeUnicode(phrase.romanized)


# def buildTextToRankDico(wordsByFreq):
# 	textToRankDico={}
# 	for word in wordsByFreq:
# 		textToRankDico[word.romanized]=word.rank
# 	return textToRankDico

# def textToRank(textToRankDico, txt):
# 	try:
# 		rank=textToRankDico[txt]
# 	except Exception as e:
# 		return 16001

# def textToWord(textToRankDico, txt):
# 	rank=textToRankDico[txt]
# 	if rank != -1:
# 		return wordsByFreq[rank]
# 	else:
# 		raise Exception('oups')

def getRank(listeWords, txt):
	if(txt==''):
		return 0
	if not (txt in listeWords):
		return 16001
	else:
		return listeWords[txt].rank

def getDico(listeWords):
	dico={}
	for expression in listeWords:
		mots = getMots(expression)
		if(len(mots) >= 2):
			ajouterExpression(dico, mots[0], expression)
	return dico

# def getAllMots(dico, txt):
# 	mots=getMots(txt.lower())
# 	for mot in mots:
# 		notYet=True
# 		if(mot in dico):
# 			for exp in dico[mot]:
# 				if isIn(exp, txt):
# 					mots.append(exp)
# 					if(notYet):
# 						mots.remove(exp)
# 						notYet=False
# 	return mots

def getAllMots(dico, txt):
	mots=getMots(txt.lower())
	for mot in mots:
		if(mot in dico):
			for exp in dico[mot]:
				if isIn(exp, txt):
					mots.append(exp)
	return mots

def getRankPhrase(listeWords, phrase, language, dico):
	txt=phrase.romanized.lower()
	mots=getAllMots(dico, txt)
	ranks=list(map(lambda a: getRank(listeWords, a), mots))
	phrase.unknownsNumber = ranks.count(16001)
	ranks = list(filter(lambda a: a != 16001, ranks))
	if(len(ranks)==0):
		phrase.rank=16001
	else:
		phrase.rank = max(ranks)

def computeRanks(phrases, language, fromEnglish):
	print('computeRanks', language)
	listeWords=getListeWords(language, fromEnglish)
	dico=getDico(listeWords)
	longueur=len(phrases)
	for index, phrase in enumerate(phrases):
		print(f'\r{index/longueur*100} %', end='', flush=True)
		getRankPhrase(listeWords, phrase, language, dico)

from functools import cmp_to_key
def compare(phrase1, phrase2):
	if (phrase1.unknownsNumber == phrase2.unknownsNumber):
		return (phrase1.rank - phrase2.rank)
	else:
		return (phrase1.unknownsNumber - phrase2.unknownsNumber)

def prettyPrint(phrasesSimples, wordsByFreq, language, fromEnglish):
	fileName=f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/wordsToPhrasesFreq_old/{language}.txt'
	if fromEnglish:
		fileName=f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/wordsToPhrasesFreq_old/english2{language}.txt'
	result = list(map(lambda a: (a.romanized, a.translation, a.rank, a.unknownsNumber), phrasesSimples))
	mySet=set()
	newResult=[]
	for p in result:
		if not p[0] in mySet:
			mySet.add(p[0])
			newResult.append(p)
	file=open(fileName,'w+')
	j=0
	for i in range(len(wordsByFreq)):
		aaa=file.write(f'--------\n[{i+1}] {wordsByFreq[i].romanized} --> {wordsByFreq[i].meaning} \n')
		while(j < len(newResult) and newResult[j][2] == i ):
			aaa=file.write(newResult[j][0] + ' --> ' + newResult[j][1] + '\n')
			j+=1
	file.close()

from statistics import mean, median
def printLogs(phrases, language, lenPhrasesSimples, fromEnglish):
	meanUnknowns = mean([c.unknownsNumber for c in phrases])
	medianUnknowns = median([c.unknownsNumber for c in phrases])
	meanRanks = mean([c.rank for c in phrases])
	medianRanks = median([c.rank for c in phrases])
	fileName=f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/logs/{language}.txt'
	if(fromEnglish):
		fileName=f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/logs/english2{language}.txt'
	file=open(fileName,'w+')
	file.write(f'mean unknowns : {meanUnknowns}\n')
	file.write(f'median unknowns : {medianUnknowns}\n')
	file.write(f'mean ranks : {meanRanks}\n')
	file.write(f'median ranks : {medianRanks}\n')
	file.write(f'length of phrases : {len(phrases)}\n')
	file.write(f'length of phrasesSimples : {lenPhrasesSimples}\n')
	file.close()

def removeDuplicates(phrases):
	print('removeDuplicates')
	mySet=set()
	newPhrases=[]
	longueur=len(phrases)
	for index,phrase in enumerate(phrases):
		print(f'\r{index/longueur*100} %', end='', flush=True)
		if not phrase.romanized in mySet:
			mySet.add(phrase.romanized)
			newPhrases.append(phrase)
	return newPhrases

def computePkl(language, fromEnglish):
	print('computePkl',language)
	if language == 'hebrew':
		phrases=getPhrasesHebrew()
	else:
		phrases=getPhrasesFromTsv(language) # ... to english
		transliterateList2(phrases, language)
	cleanup(phrases)
	phrases=removeDuplicates(phrases)
	if fromEnglish:
		for phrase in phrases:
			temp = phrase.romanized # will become destination (normally is origin of translation)
			phrase.romanized = phrase.translation
			phrase.translation = temp
	phrases=removeDuplicates(phrases)
	computeRanks(phrases, language, fromEnglish)
	phrases = sorted(phrases, key=cmp_to_key(compare))
	for index,phrase in enumerate(phrases):
		phrase.id = index
	savePhrases(phrases, language, fromEnglish)

# l=[]
# for i, phrase in enumerate(phrases):
# 	if('govo' in phrase.romanized):
# 		l.append(phrase.romanized)


def computeAllPkls():
	for language in languages:
		computePkl(language)

def computePrettyPrint(language, fromEnglish):
	print('compute prettyprint', language)
	wordsByFreq=getWordsByFreq(language, fromEnglish)
	phrases=getPhrases(language, fromEnglish)
	phrasesSimples = list(filter(lambda p: p.unknownsNumber <= 0, phrases))
	printLogs(phrases, language, len(phrasesSimples), fromEnglish)
	prettyPrint(phrasesSimples, wordsByFreq, language, fromEnglish)

def computeAllPrettyPrints():
	for language in languages:
		computePrettyPrint(language)


# =====================
# Anki


def computeWordsToPhrases(language, fromEnglish):
	phrases=getPhrases(language, fromEnglish)
	listeWords=getListeWords(language, fromEnglish)
	dico=getDico(listeWords)
	wordsToPhrases={}
	longueur=len(phrases)
	for (index,phrase) in enumerate(phrases):
		print(f'\r{index/longueur*100} %', end='', flush=True)
		mots=getAllMots(dico, phrase.romanized)
		for mot in mots:
			ajouterExpression(wordsToPhrases, mot, phrase)
	return wordsToPhrases


def computeWordsToPhrasesFinal(wordsToPhrases, language, fromEnglish):
	wordsByFreq=getWordsByFreq(language, fromEnglish)
	wordsToPhrasesFinal={}
	for index,word in enumerate(wordsByFreq):
		if not (word.romanized in wordsToPhrases):
			continue
		else:
			phrasesOfMot=wordsToPhrases[word.romanized]
			sortedPhrases = sorted(phrasesOfMot, key=cmp_to_key(compare))
			wordsToPhrasesFinal[index]=sortedPhrases[:5]
	if not fromEnglish:
		save_object(wordsToPhrasesFinal, f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/wordsToPhrasesFinal/{language}.pkl')
	else:
		save_object(wordsToPhrasesFinal, f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/wordsToPhrasesFinal/english2{language}.pkl')
	return wordsToPhrasesFinal


def writePhrasesForAnki(phrasesOfMot, file, wordsByFreq, word):
	n = len(phrasesOfMot)
	index = 0
	while index < n:
		phrase = phrasesOfMot[index]
		file.write(phrase.romanized.replace('=','~') + '=')
		file.write(phrase.translation.replace('=','~') + '=')
		if(phrase.unknownsNumber > 0):
			file.write(f' [!!! : unknown(s) word(s)]')
		if((phrase.rank > word.rank) and (phrase.rank < len(wordsByFreq))):
			file.write(f' [!!! : {wordsByFreq[phrase.rank].romanized} ({phrase.rank})]')
		if(index < 4):
			file.write('=')
		index += 1
	while index < 4:
		file.write('===')
		index+=1
	while(index < 5):
		file.write('==')
		index+=1

def prepareAnkiImport(wordsToPhrasesFinal, language, fromEnglish):
	wordsByFreq=getWordsByFreq(language, fromEnglish)
	fileName=f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/wordsToPhrases_txt/{language}.txt'
	if fromEnglish:
		fileName=f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/wordsToPhrases_txt/english2{language}.txt'
	file=open(fileName, 'w+')
	for index,word in enumerate(wordsByFreq):
		if index in wordsToPhrasesFinal:
			phrasesOfMot=wordsToPhrasesFinal[index]
		else:
			continue
		file.write(word.romanized.replace('=','~') + '=')
		file.write(word.meaning.replace('=','~') + '=')
		file.write(str(word.rank) + '=')
		writePhrasesForAnki(phrasesOfMot, file, wordsByFreq, word)
		file.write('\n')
	file.close()

def getWordsToPhrasesFinal(language, fromEnglish):
	if not fromEnglish:
		wordsToPhrasesFinal = get_object(f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/wordsToPhrasesFinal/{language}.pkl')
	else:
		wordsToPhrasesFinal = get_object(f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/wordsToPhrasesFinal/english2{language}.pkl')
	return wordsToPhrasesFinal

def computeTextForAnkiImports(language, fromEnglish):
	print('computeTextForAnkiImports', language)
	wordsToPhrases = computeWordsToPhrases(language, fromEnglish)
	wordsToPhrasesFinal = computeWordsToPhrasesFinal(wordsToPhrases, language, fromEnglish)
	# wordsToPhrasesFinal = getWordsToPhrasesFinal(language, fromEnglish)
	prepareAnkiImport(wordsToPhrasesFinal, language, fromEnglish)

def computeAllTextsForAnkiImports():
	for language in languages:
		computeTextForAnkiImports(language)

# =======================================

# by alpha :

def writePhrasesForAlpha(phrasesOfMot, file, word, numPhrases=[(3000,3)]):
	file.write(f'• {word.romanized} ({word.rank})')
	if(word.meaning != ''):
		file.write(f' --> {word.meaning}') # [:120]
	# if(len(word.meaning)>120):
	# 	file.write(' .....')
	file.write(' :: ')
	n=1
	for (rank, i) in numPhrases:
		if(word.rank < rank):
			n = i
			break
	liste=[]
	for phrase in phrasesOfMot:
		if(len(liste)>=n):
			break
		if(len(phrase.romanized) < 120 and len(phrase.translation) < 120):
			liste.append(f'{phrase.romanized} --> {phrase.translation}')
	file.write(' / '.join(liste))
	file.write('\n')


def computeAlpha(language, fromEnglish, restriction=16000, numPhrases=[(3000,3)], smallSuffix=''):
	print('compute alpha', language)
	wordsToPhrasesFinal = getWordsToPhrasesFinal(language, fromEnglish)
	wordsByFreq=getWordsByFreq(language, fromEnglish)
	wordsByFreq=wordsByFreq[:restriction]
	wordsByAlpha=getSortedByAlpha(wordsByFreq)
	fileName=f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/wordsToPhrasesAlpha/{language}{smallSuffix}.txt'
	if fromEnglish:
		fileName=f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/wordsToPhrasesAlpha/english2{language}{smallSuffix}.txt'
	file=open(fileName, 'w+')
	for word in wordsByAlpha:
		index = word.rank
		if index in wordsToPhrasesFinal:
			phrasesOfMot=wordsToPhrasesFinal[index]
		else:
			continue
		writePhrasesForAlpha(phrasesOfMot, file, word, numPhrases)
	file.close()

def computeAlphaSmall(language, fromEnglish):
	computeAlpha(language, fromEnglish, restriction=3650, numPhrases=[(2000,3),(3000,2)], smallSuffix='_small')

def computeAlpha_all():
	for language in languages:
		print(language)
		computeAlpha(language)

# ===================

def writePhrasesForFreq(phrasesOfMot, file, word):
	file.write(f'• {word.romanized} ({word.rank})')
	if(word.meaning != ''):
		file.write(f' --> {word.meaning}') # 
	# if(len(word.meaning)>120):
	# 	file.write(' .....')
	file.write(' :: ')
	n = 1
	if(word.rank < 3000):
		n = 3
	elif(word.rank < 6000):
		n = 2
	liste=[]
	for phrase in phrasesOfMot:
		if(len(liste)>=n):
			break
		if(len(phrase.romanized) < 100 and len(phrase.translation) < 100):
			liste.append(f'{phrase.romanized} --> {phrase.translation}')
	file.write(' / '.join(liste))
	file.write('\n')

def computeWordsToPhrasesFreq(language, fromEnglish):
	print('computeWordsToPhrasesFreq', language)
	wordsToPhrasesFinal = getWordsToPhrasesFinal(language, fromEnglish)
	wordsByFreq=getWordsByFreq(language, fromEnglish)
	fileName=f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/wordsToPhrasesFreq/{language}.txt'
	if fromEnglish:
		fileName=f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/wordsToPhrasesFreq/english2{language}.txt'
	file=open(fileName, 'w+')
	for word in wordsByFreq:
		index = word.rank
		if index in wordsToPhrasesFinal:
			phrasesOfMot=wordsToPhrasesFinal[index]
		else:
			continue
		writePhrasesForFreq(phrasesOfMot, file, word)
	file.close()

def computeWordsToPhrasesFreq_all():
	for language in languages:
		print(language)
		computeWordsToPhrasesFreq(language)

# ===================

import sys
sys.path.append('/Users/nicolas/Desktop/NaturaLingua/SubsToBilingualText/youtube')
from youtube import absorbYoutubeChannels
sys.path.append('/Users/nicolas/Desktop/NaturaLingua/SubsToBilingualText/movies')
from movies import allMoviesOfLanguage
sys.path.append('/Users/nicolas/Desktop/NaturaLingua/dictionaries')
from frequency import getFrequenciesLanguage
from meanings import doMeanings

# import importlib
# importlib.reload(sys.modules['meanings'])

def doAll(language):
	# absorbYoutubeChannels(language)
	# allMoviesOfLanguage(language)
	# getFrequenciesLanguage(language)
	# doMeanings(language, False)
	# computeNewWordsByFreq(language, False)
	# computePkl(language, False)
	# computePrettyPrint(language, False)
	# computeTextForAnkiImports(language, False)
	computeAlpha(language, False)
	computeAlphaSmall(language, False)
	computeWordsToPhrasesFreq(language, False)


# doAll('chinese')


# absorbYoutubeChannels('english')
# allMoviesOfLanguage('english')
# getFrequenciesLanguage('english')
def doAllFromEnglish(language):
	# print('doAllFromEnglish', language)
	# doMeanings(language, True)
	# computeNewWordsByFreq(language, True)
	# computePkl(language, True)
	# computePrettyPrint(language, True)
	# computeTextForAnkiImports(language, True)
	computeAlpha(language, True)
	computeAlphaSmall(language, True)
	computeWordsToPhrasesFreq(language, True)


import sys
sys.path.append('/Users/nicolas/Desktop/NaturaLingua/txt2pdf')
from txt2pdf import doAllPdfs_fromEnglish
# importlib.reload(sys.modules['txt2pdf'])

def doAllAllFromEnglish():
	for language in languages:
		if language != 'english':
			doAllFromEnglish(language)

def doAllAllToEnglish():
	for language in languages:
		if language != 'english':
			doAll(language)

doAllPdfs_fromEnglish()
