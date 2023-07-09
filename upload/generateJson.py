sys.path.append('/Users/nicolas/Desktop/NaturaLingua/upload')
from prices import getPrice
from isAllowed import isAllowed
from uuid import uuid4
import sys
sys.path.append('/Users/nicolas/Desktop/NaturaLingua/utils')
from utils import getListFiles, save_object

# /toEnglish/language/category/filename
# /toEnglish/language/youtube/channel/filename
files=getListFiles(['/Users/nicolas/Desktop/NaturaLingua/toEnglish/*/*/*.pdf','/Users/nicolas/Desktop/NaturaLingua/toEnglish/*/*/*.apkg','/Users/nicolas/Desktop/NaturaLingua/toEnglish/*/*/*/*.pdf'])

def getParams(filepath):
	liste=filepath.split('/')
	index=liste.index('toEnglish') # normally no exception, because files are taken from there.
	language=liste[index+1]
	category=liste[index+2]
	filename=liste[-1]
	price=getPrice(language, category, filename)
	if liste[-2] != category:
		channel = liste[-2]
	else:
		channel = ''
	id=str(uuid4())
	params={'name':filename, 'price':price, 'language':language,'category':category,"id":id,'channel':channel}
	return params	

def isAllowed(params):
	if(params['category'] == 'to english' or params['category'] == 'from english'):
		return True
	return False

dico=[]
dico2={}
for file in files:
	params=getParams(file)
	if(isAllowed(params)):
		dico.append(params)
		dico2[params['id']]=params

import json
jsonStr = json.dumps(dico)
fileJson=open('/Users/nicolas/Desktop/listOfFiles.json','w+')
fileJson.write(jsonStr)
fileJson.close()

save_object(dico2, '/Users/nicolas/Desktop/products.pkl')



# ===================

# import os

# def ajouterFichier_old(dico, language, category, fileName, dico2):
# 	if not language in dico:
# 		dico[language]={}
# 	if not category in dico[language]:
# 		dico[language][category]=[]#set()
# 	price=getPrice(language, category, fileName)
# 	dico[language][category].append({'name':fileName, 'price':price}) #.add(fileName)
# 	dico2[fileName]=price


# dico={}
# dico2={}
# root = '/Users/nicolas/Desktop/NaturaLingua/toEnglish'
# rootFolder = os.scandir(root)
# for entry in rootFolder :
# 	if entry.is_dir():
# 		language=entry.name
# 		for kindofdoc in ['movies','youtube','dictionary and co']:
# 			moviesFolderName=f'{entry.path}/{kindofdoc}'
# 			language=entry.name
# 			if(not os.path.isdir(moviesFolderName)):
# 				continue
# 			moviesFolder = os.scandir(moviesFolderName)
# 			for entry2 in moviesFolder :
# 				if entry2.is_file():
# 					if entry2.name.endswith('.pdf') or entry2.name.endswith('.zip') or entry2.name.endswith('.apkg') :
# 						if(isAllowed(language, kindofdoc, entry2.name)):
# 							ajouterFichier(dico, language, kindofdoc, entry2.name, dico2)

# dico['Korean']['movies']

