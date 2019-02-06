
def slInput(inPhrase,fgColor='bright green',bgColor=(14,22,40),startline=3,linespacing=0,command=None):
	'''
	inPhrase is the phrase that is printed as the input line
	startline is the line that the input line is on
	linespacing is the number of blank lines between output lines, default 0
	command is a function that manipulates the output, default is None
	'''

	cDict = {'black':         30,
					 'red':           31,
					 'green':         32,
					 'yellow':        33,
					 'blue':          34,
					 'magenta':       35,
					 'cyan':          36,
					 'grey':          37,
					 'gray':          37,
					 'dark grey':     90,
					 'dark gray':     90,
					 'bright red':    91,
					 'bright green':  92,
					 'bright yellow': 93,
					 'bright blue':   94,
					 'bright magenta':95,
					 'bright cyan':   96,
					 'white':         97}
	
	def color(bg,pColor):
		def rgb(r,g,b):
			return f'\033[{38+10*bg};2;{r};{g};{b}m'
		
		return f'\033[{cDict[pColor]+10*bg}m' if pColor in cDict.keys() else rgb(*pColor)

	fg = color(False,fgColor)
	bg = color(True,bgColor)

	def down(inList):
		if len(inList) == 1:
			return '\n'*linespacing
		else:
			return '\033[u'+'\n'*linespacing

	def up():
		return f'\033[s\033[{startline};H'
	
	def sl():
		inList = []
		outDict = {}

		try:
			while True:
				inList += [input(f'\033[{startline}H{fg}{bg}{inPhrase}\033[0m\033[K')]

				if command != None:
					outDict[inList[-1]] = command(inList[-1])
					print(f'{down(inList)}{list(outDict.values())[-1]}{up()}')
				else:
					print(f'{down(inList)}{inList[-1]}{up()}')
		except KeyboardInterrupt:
			print(f'{down(inList)}\033[2E')
			return outDict if command != None else inList

	return sl()

if __name__ == '__main__':
	def mult3(i):
		return int(i)*3

	out = slInput('Number: ',linespacing=2,command=mult3)
