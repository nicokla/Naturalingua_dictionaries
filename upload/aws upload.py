# https://s3.console.aws.amazon.com/s3/upload/naturalingua?region=eu-west-3

# https://stackoverflow.com/questions/30249069/listing-contents-of-a-bucket-with-boto3

# https://stackoverflow.com/questions/15085864/how-to-upload-a-file-to-directory-in-s3-bucket-using-boto

import boto3
import os
from dotenv import load_dotenv
load_dotenv('.env')

import sys
sys.path.append('/Users/nicolas/Desktop/NaturaLingua/upload/')
from isAllowed import isAllowed
sys.path.append('/Users/nicolas/Desktop/NaturaLingua/utils/')
from utils import getListFiles


session = boto3.Session(
		aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
		aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))

s3 = session.resource('s3')
bucket = s3.Bucket('naturalingua')

def getFilesFromAWS(language, category):
	cap = language.capitalize()
	liste = bucket.objects.filter(Prefix=f'toEnglish/{cap}/{category}')
	return list(map(lambda a: a.key, liste))

def isInAWS(language, category, fileName, channel):
	liste=getFilesFromAWS(language, category)
	if(channel == ''):
		answer = f'toEnglish/{language.capitalize()}/{category}/{fileName}' in liste
	else:
		answer = f'toEnglish/{language.capitalize()}/{category}/{channel}/{fileName}' in liste
	return answer

def getAllFilesFromHere():
	root='/Users/nicolas/Desktop/NaturaLingua/toEnglish'
	patterns=[f'{root}/*/*/**.pdf', f'{root}/*/*/**.zip', f'{root}/*/*/**.apkg', f'{root}/*/*/*/**.pdf']
	listeFilesFromHere = getListFiles(patterns)
	return listeFilesFromHere

def cutPath(path):
	machins = path.split('/')
	index=machins.index('toEnglish')
	language=machins[index+1]
	category=machins[index+2]
	fileName=machins[-1]
	if(machins[-2] != category):
		channel=machins[-2]
	else:
		channel=''
	return language, category, fileName, channel

def getListeOfTodos():
	liste=[]
	allFilesFromHere=getAllFilesFromHere()
	for path in allFilesFromHere:
		language, category, fileName, channel=cutPath(path)
		if(isAllowed(language, category, fileName, channel)):
			if(not isInAWS(language, category, fileName, channel)):
				liste.append((language, category, fileName, channel))
	return liste

def uploadFile(language, category, fileName, channel):
	rootMe='/Users/nicolas/Desktop/NaturaLingua'
	cap = language.capitalize()
	if(channel==''):
		pathFile=f'toEnglish/{cap}/{category}/{fileName}'
	else:
		pathFile=f'toEnglish/{cap}/{category}/{channel}/{fileName}'
	object = s3.Object('naturalingua', pathFile)
	result = object.put(Body=open(f'{rootMe}/{pathFile}', 'rb'))
	res = result.get('ResponseMetadata')
	if res.get('HTTPStatusCode') == 200:
		print(f'{pathFile} Uploaded Successfully')
	else:
		print(f'{pathFile} Not Uploaded')
	

def uploadAll():
	liste = getListeOfTodos()
	for index, (language, category, fileName, channel) in enumerate(liste):
		print(index, '/', len(liste))
		uploadFile(language, category, fileName, channel)
