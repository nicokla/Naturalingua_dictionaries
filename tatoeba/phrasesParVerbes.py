
adjectifs=['happy','sad','worried','healthy','sick','tired','angry','hungry','thirsty','scary','afraid', 'big','small','nice','good','bad','funny','interesting','busy','difficult','easy','awkward','strange','tasty','red','green','yellow','blue','white','black','strong','forbidden', 'allowed', 'ready', 'clean', 'dirty']
questions=['what','who','where','when','why','how']
pronouns=['i','you','he','she','we','they']
logic=['so', 'because', 'however', 'but']
comparison=['more', 'less', 'also','already','not anymore','again','still']
uncertaintyLevels=["i don't know", 'possible', 'maybe', 'it seems that', 'i believe that', 'for sure']
basicStuff=['there is', 'there are', 'this is', 'it is', 'that is']


verbesBasics={
	'to get dressed':{ # multi
		'present': ['get dressed', 'gets dressed', 'is getting dressed', 'are getting dressed'],
		'past':['got dressed', 'was getting dressed', 'were getting dressed']
	},
	'to be born':{ # multi
		'present': ['is born', 'are born'],
		'past':['was born', 'were born']
	},
	'to fall in love':{ # multi
		'present': ['falls in love', 'fall in love'],
		'past':['fell in love']
	},
	'to get married':{ # multi
		'present': ['gets married', 'get married', 'are getting married'],
		'past':['got married']
	},
	'to fall asleep':{ # multi
		'present': ['fall asleep', 'falls asleep'],
		'past':['fell asleep']
	},
	'to be': {
		'present': ['is', 'are'],
		'past':['was', 'were']
	},
	'to have':{
		'present': ['has', 'have'],
		'past':['had']
	},
	'to eat':{
		'present': ['eat', 'eats'],
		'past':['ate']
	},
	'to drink':{
		'present': ['drink', 'drinks'],
		'past':['drank']
	},
	'to sleep':{
		'present': ['sleep', 'sleeps'],
		'past':['slept']
	},
	'to wake up':{
		'present': ['wake up', 'wakes up'],
		'past':['woke up']
	},
	'to rest':{
		'present': ['rest', 'rests'],
		'past':['rest']
	},
	'to work':{
		'present': ['work', 'works'],
		'past':['worked']
	},
	'to wash':{
		'present': ['wash', 'washes'],
		'past':['washed']
	},
	'to study':{
		'present': ['study', 'studies'],
		'past':['studied']
	},
	'to learn about':{
		'present': ['learn about', 'learns about', 'is learning about', 'are learning about'],
		'past':['learnt']
	},
	'to teach':{
		'present': ['teach', 'teaches'],
		'past':['taught']
	},
	'to play':{
		'present': ['play', 'plays'],
		'past':['played']
	},
	'to sit':{
		'present': ['sit', 'sits'],
		'past':['sitted']
	},
	'to stand':{
		'present': ['stand', 'stands'],
		'past':['stand']
	},
	'to undress':{
		'present': ['undress', 'undresses'],
		'past':['undressed']
	},
	'to die':{
		'present': ['die', 'dies'],
		'past':['died']
	},
	'to wait':{
		'present': ['wait', 'waits'],
		'past':['waited']
	},
	'to change':{
		'present': ['change', 'changes'],
		'past':['changed']
	},
	'to become':{
		'present': ['becomes', 'become'],
		'past':['became']
	},
}


verbesPerception={
	'to see':{
		'present': ['see', 'sees'],
		'past':['saw']
	},
	'to look':{
		'present': ['look', 'looks'],
		'past':['looked']
	},
	'to hear':{
		'present': ['hear', 'hears'],
		'past':['heard']
	},
	'to listen':{
		'present': ['listen', 'listens'],
		'past':['listened']
	},
}

verbesMovement={
	'to go up':{ # multi
		'present': ['go up', 'goes up'],
		'past':['went up']
	},
	'to go down':{ # multi
		'present': ['go down', 'goes down'],
		'past':['went down']
	},
	'to go in':{ # multi
		'present': ['goes in', 'go in', 'enter', 'enters'],
		'past':['entered', 'went in']
	},
	'to go out':{ # multi
		'present': ['goes out', 'go out', 'leave', 'leaves'],
		'past':['went out', 'left']
	},
	'to come back':{ # multi
		'present': ['return', 'returns', 'come back', 'comes back'],
		'past':['returned', 'came back']
	},
	'to go':{
		'present': ['go', 'goes'],
		'past':['went']
	},
	'to run':{
		'present': ['run', 'runs'],
		'past':['ran']
	},
	'to come':{
		'present': ['come', 'comes'],
		'past':['came']
	},
	'to arrive':{
		'present': ['arrive', 'arrives'],
		'past':['arrived']
	},
	'to stay':{
		'present': ['stays', 'stay', 'is staying'],
		'past':['stayed']
	},
	'to fall':{
		'present': ['fall', 'falls'],
		'past':['fell']
	},
	'to stop':{
		'present': ['stop', 'stops'],
		'past':['stopped']
	},
}


verbesObjet={
	'to look for':{ # multi
		'present': ['look for', 'search','looks for', 'searches', 'looking for'],
		'past':['looked for']
	},
	'to lose':{
		'present': ['lose', 'loses'],
		'past':['lost']
	},
	'to find':{
		'present': ['find', 'finds'],
		'past':['found']
	},
	'to hold':{
		'present': ['hold', 'holds'],
		'past':['hold']
	},
	'to create':{
		'present': ['create', 'prepare', 'design', 'build', 'creates', 'prepares', 'designs', 'builds'],
		'past':['created', 'prepared', 'designed', 'built']
	},
	'to give':{
		'present': ['give', 'gives'],
		'past':['gave']
	},
	'to take':{
		'present': ['take', 'get', 'receive', 'takes', 'gets', 'receives'],
		'past':['took', 'got', 'received']
	},
	'to put':{
		'present': ['put', 'puts'],
		'past':['put']
	},
	'to open':{
		'present': ['open', 'opens'],
		'past':['opened']
	},
	'to close':{
		'present': ['close', 'closes'],
		'past':['closed']
	},
	'to use':{
		'present': ['use', 'uses'],
		'past':['used']
	},
	'to drop':{
		'present': ['drop', 'drops'],
		'past':['dropped']
	},
	'to buy':{
		'present': ['buy', 'buys'],
		'past':['bought']
	},
	'to throw':{
		'present': ['throw', 'throws'],
		'past':['throwed']
	},
	'to break':{
		'present': ['break', 'breaks'],
		'past':['broke']
	},
	'to fix':{
		'present': ['fix', 'fixes'],
		'past':['fixed']
	},
	'to let (an object)':{
		'present': ['let', 'lets'],
		'past':['let']
	},
}

verbesInteraction={
	'to pay':{
		'present': ['pay', 'pays'],
		'past':['payed']
	},
	'to speak':{
		'present': ['speak', 'speaks'],
		'past':['spoke']
	},
	'to ask':{
		'present': ['ask', 'asks'],
		'past':['asked']
	},
	'to answer':{
		'present': ['answer', 'answers'],
		'past':['answered']
	},
	'to say':{
		'present': ['say', 'tell', 'says', 'tells'],
		'past':['said','told']
	},
	'to explain':{
		'present': ['explain', 'explains'],
		'past':['explained']
	},
	'to agree':{
		'present': ['agree', 'agrees'],
		'past':['agreed']
	},
	'to disagree':{
		'present': ['disagree', 'disagrees'],
		'past':['disagreed']
	},
	'to visit':{
		'present': ['visit', 'visits'],
		'past':['visited']
	},
	'to read':{
		'present': ['read', 'reads'],
		'past':['read']
	},
	'to write':{
		'present': ['write', 'writes'],
		'past':['wrote']
	},
	'to help':{
		'present': ['help', 'helps'],
		'past':['helped']
	},
	'to show':{
		'present': ['show', 'shows', 'is showing', 'are showing'],
		'past':['showed', 'has shown', 'have shown']
	},
	'to meet':{
		'present': ['meet', 'meets'],
		'past':['met']
	},
}


verbesPensee={
	'to understand':{
		'present': ['understand', 'understands'],
		'past':['understood']
	},
	'to think about':{
		'present': ['think about', 'thinks about'],
		'past':['thought about']
	},
	'to know':{
		'present': ['know', 'knows'],
		'past':['knew']
	},
	'to believe':{
		'present': ['believe', 'believes'],
		'past':['believed']
	},
	'to remember':{
		'present': ['remember', 'remembers'],
		'past':['remembered']
	},
	'to forget':{
		'present': ['forget', 'forgets'],
		'past':['forgot']
	},
	'to want':{
		'present': ['want', 'wants'],
		'past':['wanted']
	},
	'to decide':{
		'present': ['decide', 'decides'],
		'past':['decided']
	},
	'to like':{
		'present': ['like', 'likes', 'love', 'loves'],
		'past':['liked','loved']
	},
	'to feel':{
		'present': ['feel', 'feels'],
		'past':['felt']
	},
}

verbesAuxiliaires={
	'to let sby do sthg':{
		'present': ['let me', 'let him', 'let her', 'let us', 'let you', 'let them'],
		'past':['let me', 'let him', 'let her', 'let us', 'let you', 'let them']
	},
	'to start doing':{
		'present': ['start', 'begin', 'starts', 'begins'],
		'past':['started']
	},
	'to continue doing':{
		'present': ['continue', 'continues'],
		'past':['continued']
	},
	'to stop doing':{ # multi !!!
		'present': ['stop', 'stops'],
		'past':['stopped']
	},
	'to resume doing':{
		'present': ['resume', 'resumes'],
		'past':['resumed']
	},
	'to finish doing':{
		'present': ['finish', 'finishes'],
		'past':['finished']
	},
	'to need to do sth':{
		'present': ['need', 'needs'],
		'past':['needed']
	},
	'to have to':{
		'present': ['have to', 'has to'],
		'past':['had to']
	},
	'to be able to':{
		'present': ['can', 'is able to', 'knows how to', 'are able to', 'know how to'],
		'past':['could', "couldn't", 'was able to', 'were able to', 'was not able to', 'were not able to', 'knew how to']
	},
	'to hope that':{
		'present': ['hope that', 'hopes that'],
		'past':['hoped that']
	},
	'to try to':{
		'present': ['try to', 'tries to'],
		'past':['tried to']
	},
	'to want to':{
		'present': ['want to', 'wants to'],
		'past':['wanted to']
	},
	'to like to':{
		'present': ['like to', 'likes to', 'loves to', 'love to'],
		'past':['liked to', 'loved to']
	},
	'to manage to':{
		'present': ['manage to', 'manages to'],
		'past':['managed to']
	},
	'to learn to':{
		'present': ['learn to', 'learns to', 'learn how to', 'learns how to'],
		'past':['learnt to', 'learnt how to']
	},
	'to say that':{
		'present': ['say that', 'says that'],
		'past':['said that']
	},
	'to think that':{
		'present': ['think that', 'thinks that', 'think we', 'think you'],
		'past':['thought that', 'thought you', 'thought we']
	},
	'to remember that':{
		'present': ['remember that', 'remembers that'],
		'past':['remembered that']
	},
	'to forget that': {
		'present': ['forget that', 'forgets that'],
		'past':['forgot that']
	},
	'to decide that':{
		'present': ['decide that', 'decides that'],
		'past':['decided that']
	},
}

verbes=[verbesAuxiliaires,verbesBasics,verbesObjet,verbesPerception,verbesMovement,verbesPensee,verbesInteraction]



# ===========================

import sys
sys.path.append('/Users/nicolas/Desktop/NaturaLingua/SubsToBilingualText')
from transliteratePerso import transliterate
from transliterateHebrew import computeRomanizedHebrew

def getCode(langue):
	dicoco={'chinese':'zh','persian':'fa','greek':'el'}
	if(langue in dicoco):
		return dicoco[langue]
	else:
		return langue[:2]

def transliterate2(word, langue):
	return transliterate(word, getCode(langue))

# transliterate("知识就是力量", 'zh')
# transliterate2("知识就是力量", 'chinese')

# -------------------------
# parse docs tatoeba

def orderByKey(unsorted_dict):
	sorted_dict = sorted(unsorted_dict.items())
	result = list(map(lambda a: a[1], sorted_dict))
	return result

def orderByValue(dict):
	step1=sorted(dict.items(), key=lambda item: item[1].count, reverse=True)
	result = list(map(lambda a: a[1], step1))
	return result


import pickle
def save_object(obj, filename):
  with open(filename, 'wb') as output:  # Overwrites any existing file.
    pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def get_object(filename):
  with open(filename, 'rb') as input:
    return pickle.load(input)

class Word:
	def __init__(self, romanized, count, rank=-1, meaning='', original=''):
		self.romanized = romanized
		self.count = count
		self.original = original
		self.rank = rank
		self.meaning = meaning
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


class PhraseTraduite:
	def __init__(self, original, translation, romanized='', rank=-1, unknownsNumber=0):
		self.original = original
		self.translation = translation
		self.romanized = romanized
		self.rank = rank # argmax (ranks connus) _ should be low to high
		self.unknownsNumber = unknownsNumber
	def __str__(self) -> str:
		return (f'{self.original} ({self.romanized}) : {self.translation}')

# phrases=[PhraseTraduite('מה נשמע', 'how are you')]
# computeRomanizedHebrew(phrases)
# phrases[0].romanized

def computeRomanized(phrases, language):
	if(langue in ['french', 'spanish', 'portuguese', 'italian', 'turkish', 'vietnamese']):
		return # no need to compute it
	if(language =='hebrew'):
		computeRomanizedHebrew(phrases)
	else:
		longueur=len(phrases)
		for index,phrase in enumerate(phrases):
			print(f'{index/longueur*100} %')
			phrase.romanized = transliterate2(phrase.original, language)

def getPhrases(langue):
	fileName=f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/tsv files/{langue}.tsv'
	f=open(fileName, "r")
	lines = f.readlines()
	liste=[]
	longueur=len(lines)
	for index, line in enumerate(lines):
		print(f'{index/longueur*100} %')
		words=line.strip().split('\t')
		liste.append(PhraseTraduite(words[1], words[3]))
	return liste

def getListeWords(langue):
	if(langue=='chinese'):
		return get_object(f'/Users/nicolas/Desktop/NaturaLingua/dictionaries_results/{langue}/meanings3.pkl')
	elif(langue=='thai'):
		return get_object(f'/Users/nicolas/Desktop/NaturaLingua/dictionaries_results/{langue}/meanings.pkl')
	else:
		return get_object(f'/Users/nicolas/Desktop/NaturaLingua/dictionaries_results/{langue}/meanings2.pkl')

def getRank(listeWords, txt):
	if(txt==''):
		return 0
	if not (txt in listeWords):
		return 16001
	else:
		return listeWords[txt].rank


def wordToString(word, langue):
	if(langue in ['french', 'spanish', 'portuguese', 'italian', 'turkish', 'vietnamese']):
		if(word.original == 'b' or word.original == ''):
			return word.romanized
		else:
			return word.original
	elif langue in ['japanese', 'russian', 'hebrew', 'arabic', 'korean', 'chinese', 'thai', 'persian', 'greek',  'hindi']:
		return word.romanized
	else:
		raise(Exception('unknown language'))


def phraseToString(phrase, langue):
	if(langue in ['french', 'spanish', 'portuguese', 'italian', 'turkish', 'vietnamese']):
		return phrase.original
	elif langue in ['japanese', 'russian', 'hebrew', 'arabic', 'korean', 'chinese', 'thai', 'persian', 'greek',  'hindi']:
		return phrase.romanized
	else:
		raise(Exception('unknown language'))

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

def getRankPhrase(listeWords, phrase, langue):
	txt=phraseToString(phrase, langue)
	mots=getMots(txt)
	ranks=list(map(lambda a: getRank(listeWords, a), mots))
	phrase.unknownsNumber = ranks.count(16001)
	ranks = list(filter(lambda a: a != 16001, ranks))
	if(len(ranks)==0):
		phrase.rank=16001
	else:
		phrase.rank = max(ranks)

def computeRanks(phrases, langue):
	listeWords=getListeWords(langue)
	longueur=len(phrases)
	for index, phrase in enumerate(phrases):
		print(f'{index/longueur*100} %')
		getRankPhrase(listeWords, phrase, langue)

def savePhrasesPkl(phrases, langue, path='/Users/nicolas/Desktop/NaturaLingua/tatoeba/pkl files'):
	filename=f'{path}/{langue}.pkl'
	save_object(phrases, filename)

def loadPhrasesPkl(langue, path='/Users/nicolas/Desktop/NaturaLingua/tatoeba/pkl files'):
	filename=f'{path}/{langue}.pkl'
	phrases = get_object(filename)
	return phrases

def stringWithoutStrangeUnicode(s):
	dico={'。':'.','،':',','؟':'?','！':'!','，':',','\xa0':' ','\u202f':' '}
	for key in dico:
		s=s.replace(key, dico[key])
	return s

def cleanup(phrases):
	if(langue in ['french', 'spanish', 'portuguese', 'italian', 'turkish', 'vietnamese']):
		for phrase in phrases:
			phrase.original = stringWithoutStrangeUnicode(phrase.original)
	else:
		for phrase in phrases:
			phrase.romanized = stringWithoutStrangeUnicode(phrase.romanized)


# phrasesClassees = sorted(phrases, key=lambda item: item.rank) # reverse=True
# phrases = sorted(phrases, key=cmp_to_key(compare))
from functools import cmp_to_key
def compare(phrase1, phrase2):
	if (phrase1.rank == phrase2.rank):
		return (phrase1.unknownsNumber - phrase2.unknownsNumber)
	else:
		return (phrase1.rank - phrase2.rank)


def ajouterExpression(dico, mot, exp):
	if not (mot in dico):
		dico[mot] = [exp]
	else:
		dico[mot].append(exp)

def getDico(listeWords):
	dico={}
	for expression in listeWords:
		mots = getMots(expression)
		if(len(mots) >= 2):
			ajouterExpression(dico, mots[0], expression)
	return dico


def getRankPhrase2(listeWords, phrase, langue, dico):
	txt=phraseToString(phrase, langue).lower()
	mots=getMots(txt)
	for mot in mots:
		if(mot in dico):
			for exp in dico[mot]:
				if exp in txt:
					mots.append(exp)
	ranks=list(map(lambda a: getRank(listeWords, a), mots))
	phrase.unknownsNumber = ranks.count(16001)
	ranks = list(filter(lambda a: a != 16001, ranks))
	if(len(ranks)==0):
		phrase.rank=16001
	else:
		phrase.rank = max(ranks)

def computeRanks2(phrases, langue):
	listeWords=getListeWords(langue)
	dico=getDico(listeWords)
	longueur=len(phrases)
	for index, phrase in enumerate(phrases):
		print(f'{index/longueur*100} %')
		getRankPhrase2(listeWords, phrase, langue, dico)

def prettyPrint(phrasesSimples, wordsByFreq, langue):
	fileName=f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/pretty prints/{langue}.txt'
	result = list(map(lambda a: (phraseToString(a, langue), a.translation, a.rank, a.unknownsNumber), phrasesSimples))
	mySet=set()
	newResult=[]
	for p in result:
		if not p[0] in mySet:
			mySet.add(p[0])
			newResult.append(p)
	file=open(fileName,'w+')
	j=0
	for i in range(len(wordsByFreq)):
		aaa=file.write(f'--------\n[{i+1}] {wordToString(wordsByFreq[i], langue)} --> {wordsByFreq[i].meaning} \n')
		while(j < len(newResult) and newResult[j][2] == (i+1) ):
			aaa=file.write(newResult[j][0] + ' --> ' + newResult[j][1] + '\n')
			j+=1
	file.close()

from statistics import mean, median
def printLogs(phrases, langue, lenPhrasesSimples):
	meanUnknowns = mean([c.unknownsNumber for c in phrases])
	medianUnknowns = median([c.unknownsNumber for c in phrases])
	meanRanks = mean([c.rank for c in phrases])
	medianRanks = median([c.rank for c in phrases])
	fileName=f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/logs/{langue}.txt'
	file=open(fileName,'w+')
	file.write(f'mean unknowns : {meanUnknowns}\n')
	file.write(f'median unknowns : {medianUnknowns}\n')
	file.write(f'mean ranks : {meanRanks}\n')
	file.write(f'median ranks : {medianRanks}\n')
	file.write(f'length of phrases : {len(phrases)}\n')
	file.write(f'length of phrasesSimples : {lenPhrasesSimples}\n')
	file.close()


# ====================================================

# 'french', 'spanish', 'portuguese','italian','turkish','vietnamese'
# ['japanese', 'russian', 'hebrew', 'arabic', 'korean', 'chinese', 'thai', 'persian', 'greek',  'hindi']
for langue in ['arabic', 'korean', 'chinese', 'thai', 'persian', 'greek',  'hindi']:
	print(langue)
	phrases=getPhrases(langue)
	listeWords=getListeWords(langue)
	wordsByFreq=orderByValue(listeWords)
	# wordsByAlpha=orderByKey(listeWords)
	computeRomanized(phrases, langue)
	computeRanks(phrases, langue)
	phrases = sorted(phrases, key=cmp_to_key(compare))
	cleanup(phrases)
	# savePhrasesPkl(phrases, langue, path='/Users/nicolas/Desktop/NaturaLingua/tatoeba/big pkl files')
	# phrases = loadPhrasesPkl(langue, path='/Users/nicolas/Desktop/NaturaLingua/tatoeba/big pkl files')
	phrasesSimples = list(filter(lambda p: p.unknownsNumber <= 0 and p.rank < 5000, phrases))
	printLogs(phrases, langue, len(phrasesSimples))
	computeRanks2(phrasesSimples, langue)
	phrasesSimples = sorted(phrasesSimples, key=cmp_to_key(compare))
	savePhrasesPkl(phrasesSimples, langue)
	# phrasesSimples=loadPhrasesPkl(langue)
	prettyPrint(phrasesSimples, wordsByFreq, langue)








# ============================

# listeWords=get_object('/Users/nicolas/Desktop/NaturaLingua/dictionaries_results/chinese/meanings.pkl')
# listeWordsByFreq=orderByValue(listeWords)
# dico={}
# for index in range(len(listeWordsByFreq)):
# 	new=listeWordsByFreq[index].romanized.replace(' ','')
# 	listeWordsByFreq[index].romanized=new
# 	dico[new]=listeWordsByFreq[index]
# save_object(dico, '/Users/nicolas/Desktop/NaturaLingua/dictionaries_results/chinese/meanings3.pkl')


# -----------------------
# import csv
# f=open(fileName, newline='')
# reader = csv.reader(f, delimiter='\t')
# i=10
# for row in reader:
# 	print(row[0])
# 	i-=1
# 	if(i<0):
# 		break


# ---------------------------------
# japanese
# docker-compose up --build
# https://github.com/himkt/konoha/blob/master/example/tokenize_demo.py
# tokenizers = ["MeCab", "KyTea", "Janome", "nagisa", "Character"]


# from konoha import WordTokenizer

# sentence = '自然言語処理を勉強しています'

# tokenizer = WordTokenizer('MeCab')
# print(tokenizer.tokenize(sentence))
# # => [自然, 言語, 処理, を, 勉強, し, て, い, ます]

# tokenizer = WordTokenizer('Sentencepiece', model_path="data/model.spm")
# print(tokenizer.tokenize(sentence))

# import cutlet
# katsu = cutlet.Cutlet()
# katsu.use_foreign_spelling = False

# def transliterateJapanese(phrase):
# 	try:
# 		return katsu.romaji(phrase)
# 	except Exception as e:
# 		return phrase

# failed :'(


# ------------------
# https://github.com/KoichiYasuoka/Japanese-LUW-Tokenizer
# from transformers import RemBertTokenizerFast
# tokenizer=RemBertTokenizerFast.from_pretrained("/Users/nicolas/Japanese-LUW-Tokenizer")
# phrase="全学年にわたって小学校の国語の教科書に大量の挿し絵が用いられている"
# tokenizer.tokenize(phrase)
# ['全', '学年', 'にわたって', '小学校', 'の', '国語', 'の', '教科書', 'に', '大量', 'の', '挿し', '絵', 'が', '用い', 'られ', 'ている', 'sal', 'ut']
# transliterate2(phrase, 'japanese')




# from statistics import mean
# from math import log


# wordsByAlpha=orderByKey(listeWords)
# wordsByFreq=orderByValue(listeWords)


# getRankPhrase : ...
# if(langue in ['french', 'spanish', 'portuguese', 'italian', 'turkish', 'vietnamese']):
# 	mots = phrase.original.split(' ')
# elif langue in ['japanese', 'russian', 'hebrew', 'arabic', 'korean', 'chinese', 'thai', 'persian', 'greek',  'hindi']:
# 	mots = phrase.romanized.split(' ')
# else:
# 	raise(Exception('unknown language'))
# for i in range(len(mots)):
# 	mots[i]=mots[i].lower()
# 	for a in ['.',',','!','?',';',':','。','،','؟','！','，','\u202f', '\xa0']:
# 		mots[i]=mots[i].replace(a, '')
