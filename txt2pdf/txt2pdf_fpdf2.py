

from fpdf import FPDF, HTMLMixin


# def chapter_title(self, label):
# 	self.set_font('Arial', '', 12)
# 	# self.set_fill_color(200, 220, 255)
# 	self.cell(0, 6, f'{label}', 0, 1, 'C', 1)
# 	self.ln(4)
# def chapter_body(self, name):
# 	with open(name, 'rb') as fh:
# 		txt = fh.read().decode('utf-8')
# 	# txt = txt.encode('latin-1', 'replace').decode('latin-1')
# 	self.set_font('Times', '', 12)
# 	self.multi_cell(0, 5, txt)
# 	self.ln()
# def prepareFont(self, language):
# if(language == 'hindi'):
# 	self.add_font('gargi', fname='gargi.ttf', uni=True) 
# 	self.set_font('gargi', size=14)
# elif(language == 'chinese' or language == 'japanese'):
# 	self.add_font('fireflysung', fname='fireflysung.ttf', uni=True)
# 	self.set_font('fireflysung', size=14)
# elif (language == 'korean'):
# 	self.add_font('eunjin', fname='Eunjin.ttf', uni=True)
# 	self.set_font('eunjin', size=14)
# elif language == 'thai':
# 	self.add_font('waree', fname='Waree.ttf', uni=True)
# 	self.set_font('waree', size=14)
# elif language in ['hebrew', 'arabic', 'greek', 'russian', 'vietnamese']:
# 	self.add_font('DejaVu', fname='DejaVuSansCondensed.ttf', uni=True)
# 	self.set_font('DejaVu', size=14)
# else:
# 	self.set_font('helvetica', size=14)

class PDF(FPDF, HTMLMixin):
	def chapter_title(self, label):
		self.write_html(f"""
  		<font size="20" color="#0000ff"><p align="center"><u><a href="{label}">{label}</a></u></p></font>
			<font size="16" color="#000000"><p align="center">Document generated with<font color="#0000ff"><u><a href="https://getyoutubesubs.netlify.app">https://getyoutubesubs.netlify.app</a></u></font> by NaturaLingua.</p></font>
			<br>
			""")
	def footer(self):
		self.set_y(-15)
		self.set_font('Arial', 'I', 8)
		self.set_text_color(128)
		self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')
	def chapter_body(self, fileName):
		txt = ''
		fh = open(fileName, 'r')
		lines = fh.readlines()
		for line in lines:
			if(not('[' in line)):
				txt+=f'{line[:-1]}<br>\n'
				continue
			i=-1
			while(line[i] != '[' and i > -15):
				i-=1
			if(i == -15):
				txt+=f'{line[:-1]}<br>\n'
				continue
			txt+=f'{line[:i]}<font color="#777777">{line[i:-1]}</font><br>\n'
		self.write_html(f'<p>\n{txt}\n</p>'.encode("ascii", "ignore").decode()) #
	def print_chapter(self, title, fileName):
		self.add_page()
		self.chapter_title(title)
		self.chapter_body(fileName)


def createPdf():
	pdf = PDF()
	fileName = f'/Users/nicolas/Desktop/truc.txt'
	pdf.print_chapter(f'https://youtu.be/z49poH6M3sg', fileName)
	output=f'/Users/nicolas/Desktop/truc.pdf'
	pdf.output(output, 'F')
	return output





# ================

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

prepareFont(pdf, 'hebrew')

text = u"""
English: Hello World
Greek: Γειά σου κόσμος
Polish: Witaj świecie
Portuguese: Olá mundo
Russian: Здравствуй, Мир
Vietnamese: Xin chào thế giới
Arabic: مرحبا العالم
Hebrew: שלום עולם
"""

for txt in text.split('\n'):
    pdf.write(8, txt)
    pdf.ln(8)

pdf.output('/Users/nicolas/Desktop/coucou.pdf')



# ===============



# https://pypi.org/project/fpdf2/

from fpdf import FPDF, HTMLMixin

class PDF(FPDF, HTMLMixin):
    pass

pdf = PDF()
# prepareFont(pdf, 'hebrew')
# らかくきこ
pdf.add_page()
pdf.write_html("""
  <h1>Big title</h1>
  <section>
    <h2>Section title</h2>
    <p><b>Hello</b> world. <u>I am</u> <i>tired</i>.</p>
		<p> קםכמרםהמר</p>
    <p><a href="https://github.com/PyFPDF/fpdf2">PyFPDF/fpdf2 GitHub repo</a></p>
    <p align="right">right aligned text</p>
    <p>i am a paragraph <br />in two parts.</p>
    <font color="#00ff00"><p>hello in green</p></font>
    <font size="7"><p>hello small</p></font>
    <font face="helvetica"><p>hello helvetica</p></font>
    <font face="times"><p>hello times</p></font>
  </section>
  <section>
    <h2>Other section title</h2>
    <ul><li>unordered</li><li>list</li><li>items</li></ul>
    <ol><li>ordered</li><li>list</li><li>items</li></ol>
    <br>
    <br>
    <pre>i am preformatted text.</pre>
    <br>
    <blockquote>hello blockquote</blockquote>
    <table width="50%">
      <thead>
        <tr>
          <th width="30%">ID</th>
          <th width="70%">Name</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td>Alice</td>
        </tr>
        <tr>
          <td>2</td>
          <td>Bob</td>
        </tr>
      </tbody>
    </table>
  </section>
""")
pdf.output("/Users/nicolas/Desktop/html.pdf")


