
# https://doc.courtbouillon.org/weasyprint/stable/first_steps.html

from weasyprint import HTML, CSS

css = CSS(string='''
body {
  font-family: sans-serif;
}
@media print {
  @page {
    margin: 0.3in;
    size: A4;
    @top-right {
      content: counter(page);
    }
  }
  @page :first {
    @top-right {
      content: "";
    }
  }
}
''')

def getColor(firstChar):
  if firstChar != '-':
    return '#CC4800'
  else:
    return '#0000FF'



def getHtml(fileName, title, isYoutube=True):
	if(isYoutube):
		debut = f"""
			<h2 style="text-align: center;"><a href="{title}">{title}</a></h2>
			<h4 style="text-align: center;">Document made with <a href="https://getyoutubesubtitles.netlify.app">https://getyoutubesubtitles.netlify.app</a></h4>
			"""
	else:
		debut = f"""
			<h4 style="text-align: center;">Document made with <a href="https://getmoviessubtitles.netlify.app">https://getmoviessubtitles.netlify.app</a></h4>
			"""
	txt = ''
	fh = open(fileName, 'r')
	lines = fh.readlines()
	wasGap=True
	numJap=0
	for index, line in enumerate(lines):
		if(len(line) <= 1):
			wasGap = True
			txt+='<br style="line-height:14px;">'
			continue
		if(line.startswith('- ')):
			numJap+=1
		shouldHaveSpace = index >= 1 and (lines[index-1].startswith('    ') and line.startswith('- '))
		if shouldHaveSpace:
			marginTop='6px'
		else:
			marginTop='0px'
		if(not('[' in line)):
			txt+= f'<p style="margin-top: {marginTop}; margin-bottom: 0px; color: {getColor(line[0])};">{line[:-1]}</p>\n'
			continue
		i=-1
		while(line[i] != '[' and i > -15):
			i-=1
		if(i == -15):
			continue
		content = ''
		if wasGap:
			content=f'<p style="margin-top: 4px; margin-bottom: 3px; color: #777777;">{line[i:-1]}</p>'
		if(index>1 and shouldHaveSpace):
			content += f'<p style="margin-top: 6px; margin-bottom: 0px; color: {getColor(line[0])};">{line[2:i]}</p>\n'
		else:
			content += f'<p style="margin-top: 0px; margin-bottom: 0px; color: {getColor(line[0])};">{line[2:i]}</p>\n'
		txt += content
		wasGap = False
	return (debut + f'<div>\n{txt}\n</div>')

import os

def createPdf(videoId, fileName, isYoutube=True):
	print('createPdf')
	title=f'https://youtu.be/{videoId}'
	myString=getHtml(fileName, title, isYoutube)
	print('myString ok')
	html = HTML(string=myString)
	return html.write_pdf(fileName+'.pdf',stylesheets=[css]) # 

fileName='/Users/nicolas/Desktop/NaturaLingua/txt2pdf/chihiro.txt'
createPdf('', fileName, False)

# ====================

# HTML(string='''
#     <h1>The title</h1>
#     <p>Content goes here
# ''')
# CSS(string='@page { size: A3; margin: 1cm }')

from weasyprint import HTML, CSS
# from weasyprint.text.fonts import FontConfiguration

# font_config = FontConfiguration()
# @font-face {
#     font-family: Gentium;
#     src: url(http://example.com/fonts/Gentium.otf);
# }
# h1 { font-family: Gentium }
css = CSS(string='''
body {
  font-family: sans-serif;
}
@media print {
  a::after {
    content: " (" attr(href) ") ";
  }
  pre {
    white-space: pre-wrap;
  }
  @page {
    margin: 0.3in;
    size: Letter;
    @top-right {
      content: counter(page);
    }
  }
  @page :first {
    @top-right {
      content: "";
    }
  }
}
''') #, font_config=font_config)
myString='''<h1>The titleק׳כק׳過酷きこ</h1>'''
html = HTML(string=myString)

html.write_pdf( '/Users/nicolas/Desktop/example.pdf', stylesheets=[css]) # , font_config=font_config


# ====================


# Brotli==1.0.9
# cffi==1.15.0
# cssselect2==0.4.1
# fonttools==4.29.1
# html5lib==1.1
# Pillow==9.0.1
# pycparser==2.21
# pydyf==0.1.2
# pyphen==0.12.0
# six==1.16.0
# tinycss2==1.1.1
# weasyprint==54.1
# webencodings==0.5.1
# zopfli==0.1.9

