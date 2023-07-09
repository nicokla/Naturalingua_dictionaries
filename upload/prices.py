
def startsWithOneOf(texte, prefixes):
	for prefix in prefixes:
		if texte.startswith(prefix):
			return True
	return False


def getPrice(language, moviesOrYoutube, fileName):
	series = ['Descendants of the sun','Shtisel','Girl from nowhere','Monkey twins']
	if startsWithOneOf(fileName, series):
		return 3
	elif(language=='Arabic'):
		return 3
	else:
		return 5
