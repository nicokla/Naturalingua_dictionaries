
import sys
sys.path.append('/Users/nicolas/Desktop/NaturaLingua/utils')
from utils import languages

import genanki
from random import randrange

style = """.card {
  font-family: arial;
  font-size: 20px;
  text-align: center;
  color: black;
  background-color: white;
}
"""

my_model = genanki.Model(
  6799624175,
  'phrasesFormat',
  fields=[
    {'name': 'mot'},
    {'name': 'tradMot'},
    {'name': 'rkMot'},
    {'name': 'phr1'},
    {'name': 'trad1'},
    {'name': 'pb1'},
    {'name': 'phr2'},
    {'name': 'trad2'},
    {'name': 'pb2'},
    {'name': 'phr3'},
    {'name': 'trad3'},
    {'name': 'pb3'},
    {'name': 'phr4'},
    {'name': 'trad4'},
    {'name': 'pb4'},
    {'name': 'phr5'},
    {'name': 'trad5'},
    {'name': 'pb5'}
  ],
  templates=[
    {
      'name': 'Hanzi First Card',
      'qfmt': """{{mot}}<br><br>
				{{phr1}}<br>
				{{phr2}}<br>
				{{phr3}}<br>
				{{phr4}}<br>
				{{phr5}}
			""",
			'afmt': """{{FrontSide}}
				<hr id=answer>
				{{tradMot}}<br><br>
				{{trad1}}<br>
				{{trad2}}<br>
				{{trad3}}<br>
				{{trad4}}<br>
				{{trad5}}
			""",
    }
  ], css=style)


def getDeckName(path):
	liste=path.split('/')
	return liste[-1][:-5]

inputsOutputs=[]
for language in languages:
	if(language=='english'):
		continue
	input1=f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/wordsToPhrases_txt/english2{language}.txt'
	output1=f'/Users/nicolas/Desktop/NaturaLingua/toEnglish/{language.capitalize()}/from english/english2{language}_sentences.apkg'
	inputsOutputs.append((input1,output1))
	input2=f'/Users/nicolas/Desktop/NaturaLingua/tatoeba/wordsToPhrases_txt/{language}.txt'
	output2=f'/Users/nicolas/Desktop/NaturaLingua/toEnglish/{language.capitalize()}/to english/{language}_sentences.apkg'
	inputsOutputs.append((input2,output2))

for input, output in inputsOutputs:
	deckName = getDeckName(output)
	file=open(input,'r')
	lines=file.readlines()
	my_deck = genanki.Deck(randrange(1e10), deckName)
	print(f'preparing {deckName}...')
	for index,line in enumerate(lines):
		print(f'\r{index/len(lines)*100} %', end='', flush=True)
		line = line[:-1]
		liste = line.split('=')
		my_deck.add_note(genanki.Note(model=my_model, fields=liste))
	print(f'saving {deckName}...')
	genanki.Package(my_deck).write_to_file(output)




