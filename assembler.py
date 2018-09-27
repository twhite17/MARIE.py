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
	"STOREI":	"2",
	"LOADI"	:	"1",
	"HALT"	:	"7"
	
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
		if filePath != None:
			self.filePath = filePath
		
		with open(self.filePath, "r") as file:
			
			text = file.read().upper().split("\n")
		
		self.code = []
		for line in text:addresses
			 self.code.append(line.split())
	
	def getDirectives(self):
		pass
	
	def getOpcodes(self):
		pass
	
	
	def parse(self):
		for lineNum in range(len(self.code)):
			line = self.code[lineNum]
			
			if line[0] in opcodes:
				
				addr = self.directives[line[1]].getHex()
				self.build.append(opcodes(line[0])+addr)
			
			elif "," in line[0]:
				directives[line[0].replace(",", "")] = Address(form="dec", addr=lineNum)
				
				if line[1] == "DEC":
					self.build.append(convert.decToHex(int(line[2]), 4))
				elif line[1] == "HEX":
					if len(line[2]) < 4:
						for i in range(4-len(line)):
							line[2] = "0"+line[2]
					self.build.append(line[2])
				

	def write(self, fileName=None):
		if fileName == None:
			fileName = self.filePath.split(".")[0]+".txt"
		
		result = ""
		for line in self.build:
			result += line + '\n'
		
		with open(fileName, "w") as file:
			file.write(result)
		



if __name__ == "__main__":
	f = input("Enter the name of file : ")
	a = Assembler(filePath=f)
	a.parse()
	a.write()
	print("Successfully assembled file \"%s\"" % (f))














