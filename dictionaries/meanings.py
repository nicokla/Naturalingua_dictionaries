
def orderByKey(unsorted_dict):
	sorted_dict = sorted(unsorted_dict.items())
	result = list(map(lambda a: a[1], sorted_dict))
	return result

def orderByValue(dict):
	step1=sorted(dict.items(), key=lambda item: item[1].count, reverse=True)
	result = list(map(lambda a: a[1], step1))
	return result


class Word:
	def __init__(self, romanized, count, rank=-1, meaning='', original=''):
		self.romanized = romanized
		self.count = count
		self.original = original
		self.rank = rank
		self.meaning = meaning
	def __str__(self) -> str:
		if self.original == '':
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


# ---------

import sys
sys.path.append('/Users/nicolas/Desktop/NaturaLingua/utils')
from utils import save_object, get_object


# ----------


def printAlpha(listeWords, langue):
	liste1=orderByKey(listeWords)
	name1=f'/Users/nicolas/Desktop/NaturaLingua/dictionaries_results/{langue}/known_alpha.txt'
	file1=open(name1,'w+')
	for word in liste1:
		if(word.meaning != ''):
			abc=file1.write(f'• {word.romanized} (rk:{word.rank}, ct:{word.count}) : {word.meaning}\n')
	file1.close()
	name1=f'/Users/nicolas/Desktop/NaturaLingua/dictionaries_results/{langue}/unknown_alpha.txt'
	file1=open(name1,'w+')
	for word in liste1:
		if(word.meaning == ''):
			abc=file1.write(f'• {word.romanized} (rk:{word.rank}, ct:{word.count})\n')
	file1.close()
	name2=f'/Users/nicolas/Desktop/NaturaLingua/dictionaries_results/{langue}/all_alpha.txt'
	file2=open(name2,'w+')
	for word in liste1:
		if(word.meaning != ''):
			abc=file2.write(f'• {word.romanized} (rk:{word.rank}, ct:{word.count}) : {word.meaning}\n')
		else:
			abc=file2.write(f'• {word.romanized} (rk:{word.rank}, ct:{word.count})\n')
	file2.close()


def printFreq(listeWords, langue):
	liste2=orderByValue(listeWords)
	name2=f'/Users/nicolas/Desktop/NaturaLingua/dictionaries_results/{langue}/all_freq.txt'
	file2=open(name2,'w+')
	for i, word in enumerate(liste2):
		if(word.meaning != ''):
			abc=file2.write(f'• {word.romanized} (ct:{word.count}) : {word.meaning}\n')
		else:
			abc=file2.write(f'• {word.romanized} (ct:{word.count})\n')
		if(i%500 == 0 and i != 0):
			abc = file2.write(f'\n\n{i}\n\n')
	file2.close()
	name2=f'/Users/nicolas/Desktop/NaturaLingua/dictionaries_results/{langue}/known_freq.txt'
	file2=open(name2,'w+')
	for i, word in enumerate(liste2):
		if(i%500 == 0 and i != 0):
				abc = file2.write(f'\n\n{i}\n\n')
		if(word.meaning != ''):
			abc=file2.write(f'• {word.romanized} (ct:{word.count}) : {word.meaning}\n')
	file2.close()
	name2=f'/Users/nicolas/Desktop/NaturaLingua/dictionaries_results/{langue}/unknown_freq.txt'
	file2=open(name2,'w+')
	for i, word in enumerate(liste2):
		if(i%500 == 0 and i != 0):
				abc = file2.write(f'\n\n{i}\n\n')
		if(word.meaning == ''):
			abc=file2.write(f'• {word.romanized} (ct:{word.count})\n')
	file2.close()
	name2=f'/Users/nicolas/Desktop/NaturaLingua/dictionaries_results/{langue}/known_freq_anki.txt'
	file2=open(name2,'w+')
	for i, word in enumerate(liste2):
		if(word.meaning != ''):
			abc=file2.write(f'{word.romanized}={word.meaning}={word.rank}={word.count}\n')
	file2.close()


def getListeWords(langue):
	# return get_object(f'/Users/nicolas/Desktop/NaturaLingua/dictionaries_results/{langue}/meanings.pkl')
	pathPkl=f'/Users/nicolas/Desktop/NaturaLingua/dictionaries_results/{langue}/freq.pkl'
	liste=get_object(pathPkl)
	listeWords={}
	for index, (rom, count) in enumerate(liste):
		newWord=Word(rom, count, rank=(index+1))
		listeWords[rom]=newWord
	return listeWords

def saveListe(listeWords, langue):
	save_object(listeWords, f'/Users/nicolas/Desktop/NaturaLingua/dictionaries_results/{langue}/meanings2.pkl')

import sys
sys.path.append('/Users/nicolas/Desktop/NaturaLingua/SubsToBilingualText/transliterate')
from transliterateAll import transliterate2

def getOriginals_old(phrase):
	parts2=phrase.split(',')
	originals=[]
	for s in parts2:
		test=s.find('{')
		test2=s.find('/')
		if(test==-1 and test2==-1):
			originals.append(s[1:])
		elif(test!=-1 and test2!=-1):
			coucou=min(test,test2)
			originals.append(s[1:(coucou-1)])
		elif(test==-1 or test2==-1):
			coucou=max(test,test2)
			originals.append(s[1:(coucou-1)])

# aaa='達する /たっする, tassuru/, 到達する /とうたつする, tōtatsu-suru/'
# aaa='καπέλο {n}, πίλος {m}'
def getOriginals(phrase, fromEnglish):
	level=0
	l=[]
	s=''
	for i, c in enumerate(phrase):
		if(level == 1):
			if c in ['/']:
				level = 0
		elif level == 2:
			if c in [']', ')', '}']:
				level=0
			if fromEnglish:
				s+=c
		else:
			if c in ['/']:
				level = 1
			elif c in ['[', '(','{']:
				level = 2
				if fromEnglish:
					s+=c
			elif(c == ','):
				if(s!=''):
					l.append(s)
				s = ''
			elif c == ' ' and (i==0 or (phrase[i-1] in [',','/']) or (phrase[i+1] in [',','/'])):
				continue
			elif c == ' ' and (not fromEnglish) and (i==0 or (phrase[i-1] in [']',')','}']) or (phrase[i+1] in ['[','(','{'])):
				continue
			else:
				s+=c
		conditionSpeciale=(not fromEnglish) and (c=='{')
		if ((i == (len(phrase) - 1) and c != ',') or conditionSpeciale):
			if(s!=''):
				l.append(s)
			s=''
	return l

def getRidOfPronounciation(txt):
	condition=True
	s = ''
	i=0
	while i <len(txt):
		c=txt[i]
		if c == '/':
			condition = not condition
		if condition and c!='/':
			if(i==0 or not(txt[i]==' ' and txt[i-1]=='/')):
				s += c
		i+=1
	return s

line1='Abadan {prop} (city in Iran) :: آبادان /âbâdân/\n'
line2='hat trick {n} (three achievements in a single game or similar) :: χατ τρικ {n}\n'
line3='hat {n} (a head covering) :: καπέλο {n}, πίλος {m}\n'
line4='hate {v} (to dislike intensely) :: μισώ, απεχθάνομαι\n'
line5='arrow {n} (projectile) :: तीर {m} /tīr/, बाण /bāṇ/\n'
line6='Angkor Wat {prop} (Cambodian temple complex) :: अंगकोर वाट /ãgkor vāṭ/\n'
line7='attack {n} (attempt to cause damage or injury) :: हमला {m} /hamlā/\n'
line8='get {v} (arrive at) :: 達する /たっする, tassuru/, 到達する /とうたつする, tōtatsu-suru/\n'
line9='get {v} (become) :: 成る /なる, naru/, ～になる /...-ni naru/, ～となる /... -to naru/\n'
line10='get {v} (fetch) :: 持ち帰る /もちかえる, mochikaeru/\n'
line11='get {v} (obtain) :: 手に入れる /てにいれる, te ni ireru/, ゲットする /getto suru/\n'
line12='get {v} (receive) :: 受け取る /うけとる, uketoru/, 貰う /もらう, morau/, 受ける /うける, ukeru/\n'
line13='be {v} (occupy a place) :: 有る /ある, aru/, 在る /ある, aru/ [for non-creatures], 居る /いる, iru/ [for creatures]'
line14='he {pron} (personal pronoun "he") :: 彼 /かれ, káre/, [both male and female] あの人 /あのひと, ano hito/, [あのかた, polite] あの方 /ano kata/, [impolite] その奴 /そのやつ, sono yatsu/, [impolite, person, animal or thing] 奴 /やつ, yatsu/, [impolite] そいつ /soitsu/'
line15='you {pron} (subject pronoun: the group being addressed) :: [generic] (discourteous if used for a superior) 貴方達 /あなたたち, anata-tachi/, [honorific] 貴方方 /あなたがた, anata-gata/, [slightly rude, occasionally generic] お前達 /おまえたち, omae-tachi/, [highly insulting] 貴様等 /きさまら, kisama-ra/ [used to be highly formal], [intimate; in business, used toward subordinates] 君達 /きみたち, kimi-tachi/'
line16='your {determiner} /joʊɹ/ (belonging to you (singular; one owner)) :: ton {m} ta {f} tes {m-p} {f-p} [informal], votre {m} {f} vos {m-p} {f-p} [formal]'
def extractInfo(line, fromEnglish=False):
	if(line[-1]=='\n'):
		line=line[:-1]
	parts=line.split('::')
	if(not fromEnglish):
		meaning=parts[0][:-1]
	else:
		meaning=parts[0][:parts[0].find(' {')]
	meaning=getRidOfPronounciation(meaning)
	originals = getOriginals(parts[1], fromEnglish)
	return originals, meaning


def addWordInDicoOfSets(dicoOfSets, key, value):
	if not key in dicoOfSets:
		dicoOfSets[key] = set()
	dicoOfSets[key].add(value)

def computeMeanings(listeWords, lines, langue, fromEnglish):
	longueur = len(lines)
	dicoOfSets={}
	for index, line in enumerate(lines):
		print(f'\r{index/longueur*100} %', end='', flush=True)
		if(line[0]=='#'):
			continue
		originals,meaning=extractInfo(line, fromEnglish)
		if(fromEnglish):
			if(meaning in listeWords):
				for original in originals:
					romanized=transliterate2(original, langue)
					addWordInDicoOfSets(dicoOfSets, meaning, romanized)
		else:
			for original in originals:
				romanized=transliterate2(original, langue)
				if(romanized in listeWords):
					addWordInDicoOfSets(dicoOfSets, romanized, meaning)
	sep = ' / '
	for key in dicoOfSets:
		listeWords[key].meaning = sep.join(dicoOfSets[key])


def doMeaningsFromEnglish(langue):
	print('doMeaningsFromEnglish', langue)
	listeWords = getListeWords('english')
	if (langue=='chinese' or langue=='thai'):
		saveListe(listeWords, 'english2'+langue)
		printAlpha(listeWords, 'english2'+langue)
		printFreq(listeWords, 'english2'+langue)
		return
	fileName=f'/Users/nicolas/Desktop/NaturaLingua/dictionaries/wikitionary_others/{langue}.txt'
	with open(fileName, "r") as f:
		lines = f.readlines()
	computeMeanings(listeWords, lines, langue, True)
	saveListe(listeWords, 'english2'+langue)
	printAlpha(listeWords, 'english2'+langue)
	printFreq(listeWords, 'english2'+langue)


def doMeanings(langue, fromEnglish=False):
	print('doMeanings', langue)
	if(fromEnglish):
		doMeaningsFromEnglish(langue)
		return
	if (langue=='chinese'):
		doChinese()
		return
	elif(langue=='thai'):
		doThai()
		return
	listeWords = getListeWords(langue)
	fileName=f'/Users/nicolas/Desktop/NaturaLingua/dictionaries/wikitionary_others/{langue}.txt'
	with open(fileName, "r") as f:
		lines = f.readlines()
	computeMeanings(listeWords, lines, langue, False)
	saveListe(listeWords, langue)
	printAlpha(listeWords, langue)
	printFreq(listeWords, langue)


def doMeanings_after(langue):
	listeWords = getListeWords(langue)
	printAlpha(listeWords, langue)
	printFreq(listeWords, langue)
























# ===================================
# russian
import csv

def doRussian():
	langue='russe'
	listeWords = getListeWords(langue)
	liste2=['adjectives','nouns','others','verbs']
	pathCsv=list(map(lambda x: f'/Users/nicolas/Desktop/NaturaLingua/dictionaries/russian/{x}.csv', liste2))
	for pathFile in pathCsv:
		with open(pathFile, newline='') as f:
			reader = csv.reader(f, delimiter='\t')
			for row in reader:
				romanized=transliterate2(row[1], 'russian')
				translation=row[2]
				if(romanized in listeWords):
					if(listeWords[romanized].meaning != ''):
						listeWords[romanized].meaning += ' / '
					listeWords[romanized].meaning += translation
	saveListe(listeWords, langue)
	printAlpha(listeWords, langue)
	printFreq(listeWords, langue)









# ===================
# hebrew



import json

def doHebrew():
	with open('/Users/nicolas/Desktop/NaturaLingua/dictionaries/dict-he-en.json') as file:
		data = json.load(file)
	langue='hebrew'
	listeWords = getListeWords(langue)
	for mot in data:
		romanized=transliterate2(mot['translated'],'hebrew')
		meaning=' / '.join(mot['translation'])
		if(romanized in listeWords):
			if(listeWords[romanized].meaning != ''):
				listeWords[romanized].meaning += ' // '
			listeWords[romanized].meaning += meaning
	saveListe(listeWords, langue)
	printAlpha(listeWords, langue)
	printFreq(listeWords, langue)




# =================
# japanese

import json

def doJapanese():
	with open('/Users/nicolas/Desktop/NaturaLingua/dictionaries/jmdict.json') as file:
		data = json.load(file)
	langue='japanese'
	listeWords = getListeWords(langue)
	longueur=len(data['words'])
	for index, word in enumerate(data['words']):
		print(f'{index/longueur*100} %')
		romanized=transliterate2(word, 'japanese')
		meaning=''
		try:
			for i,sense in enumerate(word['sense']):
				for j,subAnglais in enumerate(sense['gloss']):
					meaning+=subAnglais['text']
					if (j+1)!=len(sense['gloss']):
						meaning+=', '
				if (i+1)!=len(word['sense']):
					meaning+=' / '
		except Exception as e:
			print('oups 2')
		if(romanized in listeWords):
			if(listeWords[romanized].meaning != ''):
				listeWords[romanized].meaning += ' // '
			listeWords[romanized].meaning += meaning
	saveListe(listeWords, langue)
	printAlpha(listeWords, langue)
	printFreq(listeWords, langue)



# ======================
# portugais, francais, italien, espanol, turkish

def doTurkish():
	langue='turkish'
	listeWords = getListeWords(langue)
	fileName='/Users/nicolas/Desktop/NaturaLingua/dictionaries/tei/tur-eng.tei.txt'
	# text/body/entry[...]/form/orth
	# text/body/entry[...]/sense/cit/quote
	text = open(fileName,'r').read()
	from lxml import etree
	tree = etree.fromstring(bytes(text, encoding='utf-8'))
	elems = tree.getchildren()[1].getchildren()[0].getchildren()
	problems=0
	longueur=len(elems)
	for index, elem in enumerate(elems):
		print(f'{index/longueur*100} %')
		romanized=elem.getchildren()[0].getchildren()[0].text
		meaningList=[]
		for child in elem.getchildren():
			try:
				if(child.tag.endswith('sense')):
					meaningList.append(child.getchildren()[0].getchildren()[0].text)
			except:
				problems+=1
		meaning = ' / '.join(meaningList)
		if(romanized in listeWords):
			if(listeWords[romanized].meaning != ''):
				listeWords[romanized].meaning += ' // '
			listeWords[romanized].meaning += meaning
	saveListe(listeWords, langue)
	printAlpha(listeWords, langue)
	printFreq(listeWords, langue)






# ======================
# arabe

def doArabic():
	langue='arabe'
	listeWords = getListeWords(langue)
	fileName='/Users/nicolas/Desktop/NaturaLingua/dictionaries/tei/ara-eng.tei.txt'
	# text/body/entry[...]/form/orth
	# text/body/entry[...]/sense/cit/quote
	text = open(fileName,'r').read()
	from lxml import etree
	tree = etree.fromstring(bytes(text, encoding='utf-8'))
	elems = tree.getchildren()[1].getchildren()[0].getchildren()
	problems=0
	for index, elem in enumerate(elems):
		romanized1=''
		text=elem.getchildren()[0].getchildren()[0].text
		romanized1=''
		if(len(text)>2):
			if(text[:2] == "ال"):
				romanized1=transliterate2(text[2:],'arabic').lower().strip()
		romanized2=transliterate2(text,'arabic').lower().strip()
		meaningList=[]
		for child in elem.getchildren():
			try:
				if(child.tag.endswith('sense')):
					meaningList.append(child.getchildren()[0].getchildren()[0].text)
			except:
				problems+=1
		meaning = ' / '.join(meaningList)
		for romanized in [romanized1, romanized2]:
			if(romanized in listeWords):
				if(listeWords[romanized].meaning != ''):
					listeWords[romanized].meaning += ' // '
				listeWords[romanized].meaning += meaning
	saveListe(listeWords, langue)
	printAlpha(listeWords, langue)
	printFreq(listeWords, langue)




# =========================================
# chinois

def doChinese():
	langue='chinese'
	listeWords = getListeWords(langue)
	fileName='/Users/nicolas/Desktop/NaturaLingua/dictionaries/cedict_1_0_ts_utf-8_mdbg.txt'
	with open(fileName, "r") as f:
		lines = f.readlines()
	for index, line in enumerate(lines):
		print(f'{index/len(lines)*100} %')
		if(line[0]=='#'):
			continue
		i=0
		original=''
		while(line[i]!=' '):
			original+=line[i]
			i+=1
		romanized=transliterate2(original,'chinese')
		while line[i]!='/':
			i+=1
		meaning=line[(i+1):-2]
		if(romanized in listeWords):
			if(listeWords[romanized].meaning != ''):
				listeWords[romanized].meaning += ' // '
			listeWords[romanized].meaning += meaning
	saveListe(listeWords, langue)
	printAlpha(listeWords, langue)
	printFreq(listeWords, langue)



# =========================================
# korean

def doKorean():
	langue='korean'
	listeWords = getListeWords(langue)
	fileName='/Users/nicolas/Desktop/NaturaLingua/dictionaries/kengdic.tsv'
	with open(fileName, "r") as f:
		lines = f.readlines()
	for index, line in enumerate(lines[1:]):
		print(f'{index/len(lines)*100} %')
		words=line.split('\t')
		original=words[1]
		romanized=transliterateKorean(original)
		meaning=words[3]
		if(romanized in listeWords):
			if(listeWords[romanized].meaning != ''):
				listeWords[romanized].meaning += ' // '
			listeWords[romanized].meaning += meaning
	saveListe(listeWords, langue)
	printAlpha(listeWords, langue)
	printFreq(listeWords, langue)





# =========================================
# vietnamese

def doVietnamese():
	langue='viet'
	listeWords = getListeWords(langue)
	fileName='/Users/nicolas/Desktop/NaturaLingua/dictionaries/vi2enwikitxt.txt'
	with open(fileName, "r") as f:
		lines = f.readlines()
	for index, line in enumerate(lines):
		print(f'{index/len(lines)*100} %')
		i = 0
		romanized=''
		while(line[i]!='\t'):
			romanized+=line[i]
			i+=1
		themeaning=''
		meanings=line[i:].split('<br />')
		for meaning in meanings:
			if len(meaning) > 2:
				if meaning[0].isdigit():
					if(themeaning!=''):
						themeaning+=' / '
					themeaning+=meaning
		themeaning=themeaning.replace('[[','')
		themeaning=themeaning.replace(']]','')
		themeaning=themeaning.replace('\n','')
		if(romanized in listeWords):
			if(listeWords[romanized].meaning != ''):
				listeWords[romanized].meaning += ' // '
			listeWords[romanized].meaning += themeaning
	saveListe(listeWords, langue)
	printAlpha(listeWords, langue)
	printFreq(listeWords, langue)







# =======================
# thai

def doThai():
	langue='thai'
	listeWords = getListeWords(langue)
	fileName='/Users/nicolas/Desktop/NaturaLingua/dictionaries/yaitron.xml'
	# YAiTRON/entry[...]/translation
	# YAiTRON/entry[...]/headword
	text = open(fileName,'r').read()
	from lxml import etree
	tree = etree.fromstring(bytes(text, encoding='utf-8'))
	elems = tree.getchildren()
	problems=0
	for index, elem in enumerate(elems):
		print(f'{index/len(elems)*100} %')
		try:
			original=elem.find('headword').text
			romanized=transliterate2(original,'thai')
			elemTranslation=elem.find('translation')
			meaning=elemTranslation.text
			if(len(elemTranslation.values()) > 0):
				if(elemTranslation.values()[0] != 'eng'):
					continue
			if(romanized in listeWords):
				if(listeWords[romanized].meaning != ''):
					listeWords[romanized].meaning += ' / '
				listeWords[romanized].meaning += meaning
		except:
			problems+=1
	saveListe(listeWords, langue)
	printAlpha(listeWords, langue)
	printFreq(listeWords, langue)



