class c:
	'''
	Text colors
	'''
	green = '\033[32m'
	red = '\033[31m'
	magenta = '\033[95m'
	white = '\033[97m'
	reset = '\033[0m'


def slInput(inPhrase, startLine = 3,linespacing = 0, command = None):
	'''
	inPhrase is the phrase that is printed as the input line
	startLine is the line that the input line is on
	linespacing is the number of blank lines between output lines, default 0
	command is a function that manipulates the output, default is None
	'''

	inList = []

	def down():
		return f'\033[{startLine+(1+linespacing)*len(inList)};H'

	def up():
		return f'\033[{startLine};H'

	def sl():
		nonlocal inList

		try:
			if command != None:
				while True:
					inList += [input('\033[{0}H{1}{2}{3}\033[K'.format(
																	  startLine,
																	  c.green,
																	  inPhrase,
																	  c.reset,
																	  )
									)]
					print('{0}{1}{2}'.format(
											down(),
											command(inList[-1]),
											up()
											))
			else:
				while True:
					inList += [input('\033[{0}H{1}{2}{3}\033[K'.format(
																	  startLine,
																	  c.green,
																	  inPhrase,
																	  c.reset,
																	  )
									)]
					print('{0}{1}{2}'.format(
											down(),
											inList[-1],
											up()
											))
		
		except KeyboardInterrupt:
			print(f'{down()}\033[2E')
			return inList

	return sl()
