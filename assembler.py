"""
A Simple MARIE assembler in python 3

Why does this project exist?
	I developed this assembler (alongside an emulator) because I found it
	frustrating having to do my FIT1047 assignment in the tiny web editor
	that was provided to me. With these two tools you will be able to use
	your own editor of choice and just compile and run your code when you 
	want to test it.

"""

opcodes = {
	"ADD"	:	"3",
	"SUBT"	:	"4",
	"ADDI"	:	"B",
	"CLEAR"	:	"A",
	"LOAD"	:	"1",
	"STORE"	:	"2",
	"INPUT"	:	"5",
	"OUTPUT":	"6",
	"JUMP"	:	"9",
	"SKIPCOND"	:	"8",
	"JNS"	:	"0",
	"JUMPI"	:	"C",
	"STOREI":	"D",
	"LOADI"	:	"E",
	"HALT"	:	"7"
	
	}

includeDirective = {
	
	"ADD"	:	True,
	"SUBT"	:	True,
	"ADDI"	:	True,
	"CLEAR"	:	False,
	"LOAD"	:	True,
	"STORE"	:	True,
	"INPUT"	:	False,
	"OUTPUT":	False,
	"JUMP"	:	True,
	"SKIPCOND"	:	True,
	"JNS"	:	True,
	"JUMPI"	:	True,
	"STOREI":	True,
	"LOADI"	:	True,
	"HALT"	:	False
	
	}


import convert


class Address:
	
	def __init__(self, form="dec", addr=0):
		assert form == "dec" or form == "hex", ValueError("")
		if form == "dec":
			self.address = int(addr)
		else:	
			self.address = convert.hexToDec(start)
		
	def inc(self):
		self.address += 1
	
	def getHex(self):
		return convert.decToHex(self.address)

class Assembler:
	
	def __init__(self, filePath="untitled.mas"):
		self.directives = {}
		self.build = [] 	# this is where everything is compiled to
							# every item is an instruction with an opcode and address
		self.filePath = filePath
		self.load()
		
	def load(self, filePath=None):
		
		# loads file, capitalises all letters and splits it into a list at each newline #
		if filePath != None:
			self.filePath = filePath
		
		with open(self.filePath, "r") as file:
			
			text = file.read().upper().split("\n")
		
		
		
		# Removes Comments #######################################
		ntext = []
		for line in text:
			nline = ""
			for ch in line:
				if ch != "/":
					nline += ch
				else:
					break
			ntext.append(nline)		
		text = ntext
		
		
		# Removes empty lines so program takes up less space #
		self.code = []
		for line in text:
			if line != "":
				
				x = line.split()
				
				if x != []:
				
					self.code.append(x)
		
		
		
		# where all the assembled code is stored ##############
		self.build = ["" for i in range(len(self.code))] # there isn't actually any code yet 
		
		
	def getDirectives(self):
		ADRLookup = {}
		
		for lineNum in range(len(self.code)):
			
			try:
				line = self.code[lineNum]
				if "," in line[0]:
					self.directives[line[0].replace(",", "")] = Address(form="dec", addr=lineNum)

					if line[1] == "DEC":

						self.build[lineNum] = convert.decToHex(int(line[2]), 4)

					elif line[1] == "HEX":

						line[2] = convert.minHexLength(line[2], 4)
						self.build[lineNum] = line[2]

					elif line[1] == "ADR":

						ADRLookup[line[2]] = lineNum


					self.code[lineNum][0] = self.code[lineNum][1]
					self.code[lineNum][1] = self.code[lineNum][2]

				elif line[0] == "DEC":

					self.build[lineNum] = convert.decToHex(int(line[1]), 4)

				elif line[0] == "HEX":
					line[1] = convert.minHexLength(line[1], 4)
					self.build[lineNum] = line[1]

				elif line[0] == "ADR":
					ADRLookup[line[1]] = lineNum
			except Exception as e:
				r = ""
				print(e)
				for i in self.code[lineNum]:
					r += i + " "
				print("Exception detected in line "+str(lineNum)+ " "+r)
				
		
		for direct in ADRLookup:
			self.build[ADRLookup[direct]] = convert.minHexLength(self.directives[direct].getHex(), 4)
	
	def assemble(self):
		for lineNum in range(len(self.code)):
			line = self.code[lineNum]
			if line[0] in opcodes:
				
				if includeDirective[line[0]]:
					try:
						addr = self.directives[line[1]].getHex()
					except KeyError:
						addr = line[1]
					self.build[lineNum] = opcodes[line[0]]+addr
				else:
					self.build[lineNum] = opcodes[line[0]]+"000"
	
				
			
	
	def parse(self):
		self.getDirectives() # loads all directives into a dict for usage in second parse
		self.assemble() # actually assembles code
				

	def write(self, fileName=None):
		if fileName == None:
			fileName = self.filePath.split(".")[0]+".txt"
		
		result = ""
		for line in self.build:
			result += line + '\n'
		
		with open(fileName, "w") as file:
			file.write(result[:-1])
		



if __name__ == "__main__":
	f = input("Enter the name of file : ")
	a = Assembler(filePath=f)
	a.parse()
	a.write()
	print("Successfully assembled file \"%s\"" % (f))














