

import collections
dico=[{},{},{},{},{},{}]
for i in [3,4,5]:
	fileName=f'/Users/nicolas/Desktop/interets/SubsToBilingualText/websites/results/takoboto_N{i}.txt'
	with open(fileName, "r") as f:
		lines = f.readlines()
	for line in lines:
		dico[i][line]='a'

for i in [3]:
	file2Name=f'/Users/nicolas/Desktop/interets/SubsToBilingualText/websites/results/takoboto_M{i}.txt'
	file2=open(file2Name,'w+')
	od = collections.OrderedDict(sorted(dico[i].items()))
	for k, v in od.items():
		if(not (k in dico[4] or k in dico[5])):
			file2.write(k)
	file2.close()

k='Akarui=明るい=4.24=light, well-lit, well-lighted'
not (k in dico[4]) and not (k in dico[5])
dico[3][1]





# -----------------------------------
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from lxml import html

# https://takoboto.jp/lists/study/n5vocab/?page=11
websites={}
for s, nb in [('n5',12)]:#, ('n4',12), ('n3',63)]:
	websites[s]=[]
	for i in range(nb):
		print(f'{s}, {i+1}')
		website=f"https://takoboto.jp/lists/study/{s}vocab/?page={i+1}"
		page = requests.get(website, verify = False)
		tree = html.fromstring(page.content)
		websites[s].append(tree)

import cutlet
katsu = cutlet.Cutlet()
katsu.use_foreign_spelling = False
from wordfreq import zipf_frequency

for s in ['n5']: # 'n4', 'n3'
	fileName=f'/Users/nicolas/Desktop/{s}.txt'
	file = open(fileName, 'w+')
	for tree in websites[s]:
		for a in range(50):
			try:
				element1=tree.xpath(f'//*[@id="ResultWord{a}"]/div[1]/span[1]')[0]
				mot=element1.text
				romaji=katsu.romaji(mot)
				element2=tree.xpath(f'//*[@id="ResultWord{a}"]/div[3]')[0]
				anglais=element2.text_content()
				frequency=zipf_frequency(mot, 'ja')
				line = f"{romaji}={mot}={frequency}={anglais}"
				octets=file.write(line+'\n')
			except Exception as e:
				continue
	file.close()

		













#----------------------------------------------------
# https://github.com/FooSoft/anki-connect

# -----------------------------
# DONE: podcast Jun Senesac


# https://hapaeikaiwa.com/blog/category/podcast-column/page/1
# https://hapaeikaiwa.com/blog/category/podcast-column/page/5/
# /html/body/div[1]/div[1]/div/div[2]/dl[1]/dt/h1/a
# /html/body/div[1]/div[1]/div/div[2]/dl[90]/dt/h1/a

# https://hapaeikaiwa.com/blog/2016/03/13/%e7%ac%ac92%e5%9b%9e%e3%80%8c%e6%96%87%e6%b3%95%e3%81%a8%e4%bc%9a%e8%a9%b1%e3%81%ae%e9%96%a2%e4%bf%82%e3%80%8d/
# root=/html/body/div[1]/div[1]/div/article/div
# - dialogue : paragraphes apres titre
# .../h4[1]
# .../p[6]/span[2]/text()
# - question english (li++) en, ja:
# .../ol[1]/li[1]/b
# .../ol[1]/li[1]/em
# - answers (li++) en, ja:
# .../ol[2]/li[1]/b
# .../ol[2]/li[1]/em
# - resumé (apres h4 contains Summary cad h4[4], jusqu'a h4[5])
# .../h4[4]
# .../p[30]/span/b
# .../p[30]/em
# .../h4[5]
# - fichier son
# .../p[3]/a[1]

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from lxml import html

links=[]
for i in range(5,0,-1):
  link = 'https://hapaeikaiwa.com/blog/category/podcast-column/page/'+str(i)
  page = requests.get(link, verify = False)
  tree = html.fromstring(page.content)
  for j in range(90,0,-1):
    try:
      path = '/html/body/div[1]/div[1]/div/div[2]/dl['+str(j)+']/dt/h1/a'
      links.append(tree.xpath(path)[0].get('href'))
    except Exception as e:
      continue


import cutlet
katsu = cutlet.Cutlet()
katsu.use_foreign_spelling = False

# https://stackoverflow.com/questions/57126286/fastest-parallel-requests-in-python
# https://lxml.de/lxmlhtml.html

# dialogue
def getDialogue(titleElementDialogue):
  dialogue=[]
  el=titleElementDialogue.getnext()
  while(el.tag != 'h4'):
    children=el.getchildren()
    if(el.tag == 'p' and len(children) >= 2):
      dialogue.append((children[0].text,children[1].text))
    el=el.getnext()
  return dialogue

# summary
def getSummary(titleElementSummary):
  summary=[]
  el=titleElementSummary.getnext()
  while(el.tag != 'h4'):
    if(el.tag == 'p' and len(el.getchildren()) >= 2):
      anglais=el.xpath('span/b')[0].text # el.getchildren()[0][0].text
      japonais=el.xpath('em')[0].text
      summary.append((katsu.romaji(japonais),anglais))
    el=el.getnext()
  return summary

# questions and answers
def getQuestionsAnswers(root, index):
  questions=[]
  for j in range(1,10):
    try:
      anglais=root.xpath('ol['+str(index)+']/li['+str(j)+']/b')[0].text
      japonais=root.xpath('ol['+str(index)+']/li['+str(j)+']/em')[0].text
      questions.append((katsu.romaji(japonais),anglais))
    except Exception as e:
      break
  return questions


def writeFile(fileName,linkSound,dialogue,questions,answers,summary):
  file1 = open(fileName,"w+")
  file1.write(linkSound+'\n\n\n')
  for person, sentence in dialogue:
    try:
      file1.write(person+'\n    '+sentence+'\n')
    except Exception as e:
      continue
  file1.write('\n\n')
  for i in range(len(questions)):
    try:
      questionJap=questions[i][0]
      questionEng=questions[i][1]
      answerJap=answers[i][0]
      answerEng=answers[i][1]
      file1.write(questionJap+'\n    '+questionEng+'\n')
      file1.write(answerJap+'\n    '+answerEng+'\n\n')
    except Exception as e:
      continue
  file1.write('\n\n')
  for jap, eng in summary:
    try:
      file1.write(jap+'\n    '+eng+'\n')
    except Exception as e:
      continue
  file1.close()


indexLink=0
for link in links:
  indexLink+=1
  print(indexLink)
  try:
    page = requests.get(link, verify = False)
    tree = html.fromstring(page.content)
    path = '/html/body/div[1]/div[1]/div/article/div'
    root=tree.xpath(path)[0]
    titlesElements=root.findall('h4')
    dialogue=getDialogue(titlesElements[0])
    summary=getSummary(titlesElements[3])
    linkSound=root.xpath('p[3]/a[1]')[0].get('href')
    questions=getQuestionsAnswers(root,1)
    answers=getQuestionsAnswers(root,2)
    fileName="/Users/nicolas/Desktop/senesac/"+ str(indexLink) +".txt"
    writeFile(fileName,linkSound,dialogue,questions,answers,summary)
  except Exception as e:
    print("snif :(")
    continue










# ------------------------------------------

# TODO: Grammar test (complications)


# https://japanesetest4you.com/category/jlpt-n4/jlpt-n4-grammar-test/
# https://japanesetest4you.com/category/jlpt-n3/jlpt-n4-grammar-test/page/2/
# /html/body/div[2]/div[3]/div[1]/div[1]/h2/a
# /html/body/div[2]/div[3]/div[1]/div[2]/h2/a
# /html/body/div[2]/div[3]/div[1]/div[3]/h2/a
# https://japanesetest4you.com/japanese-language-proficiency-test-jlpt-n3-grammar-exercise-21/
# https://japanesetest4you.com/japanese-language-proficiency-test-jlpt-n3-grammar-exercise-3/
# N5 : 26, N4 : 30, N3 : 29
# questions :
# /html/body/div[2]/div[3]/div[1]/div/div[2]/form/p[11]
# /html/body/div[2]/div[3]/div[1]/div/div[3]/p[1]
# /html/body/div[2]/div[3]/div[1]/div/div[3]/p[10]
# reponses :
# /html/body/div[2]/div[3]/div[1]/div/div[2]/p[4]/text()[1]
# /html/body/div[2]/div[3]/div[1]/div/div[3]/p[34]/strong       'Answer Key:'
# /html/body/div[2]/div[3]/div[1]/div/div[3]/p[35]/text()[1]
# Answer Key:
# Answer keys can be found at the bottom of this post

# 'Question 1: '
# '10. '


import cutlet
katsu = cutlet.Cutlet()
katsu.use_foreign_spelling = False
from lxml import html
import requests
import traceback
import logging

l = ['https://japanesetest4you.com/category/jlpt-n5/jlpt-n5-grammar-test/',
'https://japanesetest4you.com/category/jlpt-n5/jlpt-n5-grammar-test/page/2/',
'https://japanesetest4you.com/category/jlpt-n4/jlpt-n4-grammar-test/',
'https://japanesetest4you.com/category/jlpt-n4/jlpt-n4-grammar-test/page/2/',
'https://japanesetest4you.com/category/jlpt-n3/jlpt-n3-grammar-test',
'https://japanesetest4you.com/category/jlpt-n3/jlpt-n3-grammar-test/page/2/']
l2=[20,6,20,10,20,9]

    # questionsKanjiPath='/html/body/div[2]/div[3]/div[1]/div/div[2]/form'
    # reponsesPath='/html/body/div[2]/div[3]/div[1]/div/div[2]/p[4]'
    # motJaponais=katsu.romaji(motJaponaisKanji)
    # phraseJaponaise1Kanji=str(coucou.xpath('div[2]/div[1]/div[2]/p[1]/span')[0].text_content())


file1 = open("/Users/nicolas/Desktop/truc.txt","w+")
logfile = open("/Users/nicolas/Desktop/log.txt","w+")
a=-1
for adresse in l:
  a+=1
  print('\n##########\n'+adresse+'\n########')
  try:
    page = requests.get(adresse, verify = False)
  except Exception as e:
    logfile.write('#########\n'+traceback.format_exc()+'\n') # logging.error
    continue
  tree = html.fromstring(page.content)
  for i in range(5, l2[a]+1):
    try:
      linkObjectPath ='/html/body/div[2]/div[3]/div[1]/div['+str(i)+']/h2/a'
      machin = tree.xpath(linkObjectPath)[0].get('href')
      print('\n--> '+machin)
      # input("Press Enter to continue...")
      page2 = requests.get(machin, verify = False)
    except Exception as e:
      logfile.write('\n----------')
      logfile.write('\nlinkObjectPath: '+ linkObjectPath)
      logfile.write('\nmachin: '+ machin)
      logfile.write('\n'+traceback.format_exc())
      # logging.error(traceback.format_exc())
      continue
    tree2 = html.fromstring(page2.content)
    j=0
    while j < 11:
      j+=1
      try:
        blabla = tree2.xpath('/html/body/div/div[3]/div[1]/div/div[2]/p['+str(j)+']/strong/text()')[0]
        if(blabla == 'Example sentences:'):
          break
      except Exception as e:
        continue
    while j<85:
      j+=1 # j+=2
      try: 
        machin21 = tree2.xpath('/html/body/div/div[3]/div[1]/div/div[2]/p['+str(j)+']/text()[2]')[0]
        machin22 = tree2.xpath('/html/body/div/div[3]/div[1]/div/div[2]/p['+str(j)+']/text()[3]')[0]
        file1.write(machin22[1:]+'='+machin21[1:]+'\n')
      except Exception as e:
        continue

logfile.close()
file1.close()














# ----------------------------------------
# Done : core japanese 1000

import cutlet
katsu = cutlet.Cutlet()
katsu.use_foreign_spelling = False

# i de 1 a 10
def fileName(i):
  return 'Japanese Core 6000 _ Japanese Core 1000 _ Japanese Core 1000_ Step '+str(i)+' - iKnow!'
def fileNameFull(i):
  return '/Users/nicolas/Desktop/'+fileName(i)+'.html'
fileBig=open('/Users/nicolas/Desktop/coucou.txt','w+')
aaa=0
for i in range(1,11):
  file=open(fileNameFull(i), 'r')
  text=file.read()
  file.close()
  # page = requests.get('https://iknow.jp/courses/566922', verify = False)
  tree = html.fromstring(text) #page.content
  for j in range(1,101):
    aaa+=1
    try:
      coucou = tree.xpath('/html/body/div[2]/div/div/section/div/section/div/div/ul/li['+str(j)+']')[0]
      motAnglais=str(coucou.xpath('div[1]/div[3]/p[2]')[0].text_content())
      motJaponaisKanji=str(coucou.xpath('div[1]/div[3]/p[1]/a')[0].text_content())
      motJaponais=katsu.romaji(motJaponaisKanji)
      phraseJaponaise1Kanji=str(coucou.xpath('div[2]/div[1]/div[2]/p[1]/span')[0].text_content())
      phraseJaponaise1=katsu.romaji(phraseJaponaise1Kanji)
      phraseJaponaise2Kanji=str(coucou.xpath('div[2]/div[2]/div[2]/p[1]/span')[0].text_content())
      phraseJaponaise2=katsu.romaji(phraseJaponaise2Kanji)
      phraseAnglaise1=str(coucou.xpath('div[2]/div[1]/div[2]/p[3]')[0].text_content())
      phraseAnglaise2=str(coucou.xpath('div[2]/div[2]/div[2]/p[3]')[0].text_content())
      fileBig.write(motJaponais+'=')
      fileBig.write(phraseJaponaise1+'=')
      fileBig.write(phraseJaponaise2+'=')
      fileBig.write(motAnglais+'=')
      fileBig.write(phraseAnglaise1+'=')
      fileBig.write(phraseAnglaise2+'\n')
      print(str(aaa)+', youpi')
    except Exception as e:
      print(str(aaa)+', snif')
      input("Press Enter to continue...")
      continue
fileBig.close()










# ------------------------------------------------------
# Done : N4 et N5 grammar sentences, from japanesetest4you


from lxml import html
import requests
import traceback
import logging

l = ['https://japanesetest4you.com/jlpt-n5-grammar-list/',
'https://japanesetest4you.com/jlpt-n4-grammar-list/']
l2=[54,109]

file1 = open("/Users/nicolas/Desktop/truc.txt","w+")
logfile = open("/Users/nicolas/Desktop/log.txt","w+")
a=-1
for adresse in l:
  a+=1
  print('\n##########\n'+adresse+'\n########')
  try:
    page = requests.get(adresse, verify = False)
  except Exception as e:
    logfile.write('#########\n'+traceback.format_exc()+'\n') # logging.error
    continue
  tree = html.fromstring(page.content)
  for i in range(5, l2[a]+1):
    try:
      linkObjectPath ='/html/body/div[2]/div[3]/div[1]/div/div/p['+str(i)+']/a'
      machinHehe = tree.xpath(linkObjectPath)
      machin = machinHehe[0].get('href')
      machinSalut = tree.xpath('/html/body/div[2]/div[3]/div[1]/div/div/p['+str(i)+']/a/text()')[0]
      machinCoucou = tree.xpath('/html/body/div[2]/div[3]/div[1]/div/div/p['+str(i)+']/text()')[0]
      print('\n--> '+machin)
      # input("Press Enter to continue...")
      page2 = requests.get(machin, verify = False)
    except Exception as e:
      logfile.write('\n----------')
      logfile.write('\nlinkObjectPath: '+ linkObjectPath)
      logfile.write('\nmachin: '+ machin)
      logfile.write('\n'+traceback.format_exc())
      # logging.error(traceback.format_exc())
      continue
    tree2 = html.fromstring(page2.content)
    j=0
    while j < 11:
      j+=1
      try:
        blabla = tree2.xpath('/html/body/div/div[3]/div[1]/div/div[2]/p['+str(j)+']/strong/text()')[0]
        if(blabla == 'Example sentences:'):
          break
      except Exception as e:
        continue
    while j<85:
      j+=1 # j+=2
      try: 
        machin21 = tree2.xpath('/html/body/div/div[3]/div[1]/div/div[2]/p['+str(j)+']/text()[2]')[0]
        machin22 = tree2.xpath('/html/body/div/div[3]/div[1]/div/div[2]/p['+str(j)+']/text()[3]')[0]
        file1.write(machin22[1:]+'='+machin21[1:]+'   [[ '+machinSalut+machinCoucou+' ]]'+'\n')
      except Exception as e:
        continue

logfile.close()
file1.close()








# ----------------------------
# Done : N4 et N5 grammar sentences, from jlptsensei

from lxml import html
import requests
import traceback
import logging


nums=[5,4,3]
tailles=[3,4,5]
l=[]
for a in [0,1,2]:
  myNum = nums[a]
  for b in range(1,tailles[a]+1):
    myString = 'https://jlptsensei.com/jlpt-n' + str(myNum) + '-grammar-list/page/' + str(b)
    l.append(myString)

'//*[@id="outbrain_widget_0"]/div/div[1]/div'
'//*[@id="jl-grammar"]/tbody/tr[21]/td[2]/a'
'//*[@id="jl-grammar"]/tbody/tr[19]/td[2]/a'
'//*[@id="jl-grammar"]/tbody/tr[41]/td[2]/a'
l2=[]
for i in range(1,20):
  l2.append(i)
for i in range(21, 42):
  l2.append(i)

file1 = open("/Users/nicolas/Desktop/truc.txt","w+")
logfile = open("/Users/nicolas/Desktop/log.txt","w+")
for adresse in l:
  print('\n##########\n'+adresse+'\n########')
  try:
    page = requests.get(adresse, verify = False)
  except Exception as e:
    logfile.write('######\nsnif ouin ouin 1: '+l0)
    logging.error(traceback.format_exc())
    logfile.write('#########\n\n')
    continue
  tree = html.fromstring(page.content)
  for i in l2:
    linkObjectPath = '//*[@id="jl-grammar"]/tbody/tr['+str(i)+']/td[2]/a'
    machinHehe = tree.xpath(linkObjectPath)
    if(len(machinHehe) == 0):
      break
    machin = machinHehe[0].get('href')
    machinSalut = tree.xpath('//*[@id="jl-grammar"]/tbody/tr['+str(i)+']/td[2]/a/text()')[0]
    machinCoucou = tree.xpath('//*[@id="jl-grammar"]/tbody/tr['+str(i)+']/td[4]/text()')[0]
    print('\n--> '+machin)
    try:
      page2 = requests.get(machin, verify = False)
    except Exception as e:
      logfile.write('snif ouin ouin 2: '+machin)
      logging.error(traceback.format_exc())
      continue
    tree2 = html.fromstring(page2.content)
    j=0
    while j<20:
      j+=1
      machin21 = tree2.xpath('//*[@id="example_'+str(j)+'_romaji"]/div/text()')
      machin22 = tree2.xpath('//*[@id="example_'+str(j)+'_en"]/div/text()')
      if(len(machin21) == 0):
        break
      else: #file1.write
        file1.write(machin21[0]+'='+machin22[0]+'   [[ '+machinSalut+' ___ '+machinCoucou+' ]]'+'\n')
logfile.close()
file1.close()






# -----------------------------------
# Done : Hebrew verbs from pealim

# wb = openpyxl.Workbook()
# sheet1=wb.active
# sheet2=wb.create_sheet()

ll=["INF-L","AP-ms","AP-fs","AP-mp","AP-fp","PERF-1s",
"PERF-2ms","PERF-2fs","PERF-3ms","PERF-3fs","PERF-1p",
"PERF-2mp","PERF-3p","IMPF-1s","IMPF-2ms","IMPF-2fs",
"IMPF-3ms","IMPF-1p","IMPF-2mp","IMPF-3mp","IMP-2ms","IMP-2fs","IMP-2mp"]

#2809
for a in range(1,10):
    page = requests.get('http://www.pealim.com/dict/'+str(a))
    
    if page.content != '':
        tree = html.fromstring(page.content)
        lead = tree.xpath('//div[@class="lead"]/text()')
        if lead!=['The page you are looking for cannot be found.']:
            typ=tree.xpath('/html/body/div/div[1]/p[1]/text()')[0]
            if typ[0:4]==u'Verb':
                translation=lead[0]
                binyan = tree.xpath('/html/body/div/div[1]/p[1]/b/text()')[0]
                menukad=[]
                francais=[]
                for b in ll:
                    txt1=tree.xpath("//*[@id=\""+b+"\"]/div[1]/div[2]/text()[1]")
                    if(txt1!=[]):
                        txt1=txt1[0]
                        txt2=tree.xpath("//*[@id=\""+b+"\"]/div[1]/div[2]/b/text()")[0]
                        txt3_temp=tree.xpath("//*[@id=\""+b+"\"]/div[1]/div[2]/text()[2]")
                        if txt3_temp==[]:
                            txt3=''
                        else:
                            txt3=txt3_temp[0]
                        francais.append(txt1+txt2+txt3)
                        menukad.append(
                          tree.xpath(
                            "//*[@id=\""+b+"\"]/div[1]/div[1]/span[@class=\"menukad\"]/text()")[0])
                    
                roots=tree.xpath("/html/body/div/div[1]/p[2]/span/text()")[0]
                roots_sep=roots.rsplit(' - ')
                while len(roots_sep)<4:
                    roots_sep.append('')
                roots_sep.reverse()
                
                # num, meaning, binyan, root letters, conjugation
                aaa=[str(a),translation,binyan]+roots_sep
                sheet1.append(aaa+menukad)
                sheet2.append(aaa+francais)
                print(str(a)+" : ok")
            else:
                print(str(a)+" : not a verb")
        else:
            print(str(a)+" : echec")
    else:
        print(str(a)+" : echec de type 2")


cd "/Users/nicolas/Desktop/"
pwd
wb.save("Pealim_verbs.xlsx")