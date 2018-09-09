

import convert

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

class Value:
	
	def __init__(self, maxHexLen = 4):
		self._dec = 0
		self._hex = "0"*maxHexLen
		self.maxHexLen = maxHexLen
	
	def setHex(self, val):
		self._hex = val
		self._dec = convert.hexToDec(val)
		if len(self._hex) > self.maxHexLen:
			for n in range(len(self._hex) - self.maxHexLen):
				self._hex = self._hex[1:]
		if len(self._hex) < self.maxHexLen:
			for n in range(self.maxHexLen - len(self._hex)):
				self._hex = "0" + self._hex
				
		self._dec = convert.hexToDec(self._hex)
	
	def setDec(self, val):
		self._hex = convert.decToHex(val, self.maxHexLen)
		self._dec = val
	
	def getHex(self):
		return self._hex
	
	def getDec(self):
		return self._dec
	
	def __getitem__(self, index):
		return self._hex[index]

class Memory:
	
	def __init__(self):
		self.data = [[[Value() for i in range(16)] for i2 in range(16)] for i in range(16)]
	
	def print(self, form="dec"):
		
		sect = ""
		
		
		for x in self.data:
			
			block = ""
			
			for y in x:
				
				row = ""
				
				for z in y:
					
					row += " "+format(z.getDec(), "03d")+" "
				
				block += row + "\n"
		
			sect += block + "\n" +("-"*80)+ "\n"
			
		print(sect)
	
	def loadAddr(self, addr):
		return self.data[convert.hexToDec(addr[0])][convert.hexToDec(addr[1])][convert.hexToDec(addr[2])].getHex()
	
	def storeAddr(self, addr, val):
		self.data[convert.hexToDec(addr[0])][convert.hexToDec(addr[1])][convert.hexToDec(addr[2])].setHex(val)
		

class Emulator:
	
	def __init__(self, inp = None, fileName=None):
		#assert not (inp == None and fileName == None), AssertionError("One of inp or fileName must be non Nonetype.")
		self.memory = Memory()
		self.AC 	= Value()
		self.IR 	= Value()
		self.MAR 	= Value(3)
		self.MBR 	= Value()
		self.PC 	= Value(3)
		self.IN 	= Value()
		self.OUT 	= Value()
		
		if inp == None:
			f = open(fileName, "r")
			c = f.read()
			c = c.split("\n")
			self.loadProgram(c)
			
		elif fileName == None:
			self.loadProgram(inp)
		
		#self.memory.print()
	
	def loadProgram(self, data):
		x, y, z = 0, 0, 0
		for line in data:
			
			addr = convert.decToHex(x, 1)+convert.decToHex(y, 1)+convert.decToHex(z, 1)
			self.memory.storeAddr(addr, line)
			
			z += 1
			if z >= 16:
				z = 0
				y += 1
				
				if y >= 16:
					y = 0
					x += 1
			
		
	def __iter__(self):
		self.PC.setHex("000")
		return self
	
	def __next__(self):
		
		#print(self.memory.loadAddr(self.PC.getHex()))
		self.IR.setHex(self.memory.loadAddr(self.PC.getHex()))
		#print(self.IR.getHex())
		
		ins = self.IR.getHex()[0]
		
		#print(ins)
		
		X = self.IR.getHex()[1:]
		
		if opcodes["ADD"] == ins:
			self.MAR.setHex(X)
			self.MBR.setHex(self.memory.loadAddr(self.MAR.getHex()))
			self.AC.setDec(self.AC.getDec() + self.MBR.getDec())
			
			
			
		elif opcodes["SUBT"] == ins:
			self.MAR.setHex(X)
			self.MBR.setHex(self.memory.loadAddr(self.MAR))
			self.AC.setDec(self.AC.getDec() - self.MBR.getDec())
			
			
		elif opcodes["ADDI"] == ins:
			
			pass
		elif opcodes["CLEAR"] == ins:
			
			pass
		elif opcodes["LOAD"] == ins:
			
			pass
		elif opcodes["STORE"] == ins:
			
			pass
		elif opcodes["INPUT"] == ins:
			
			pass
		elif opcodes["OUTPUT"] == ins:
			print(self.AC.getDec())
			
		elif opcodes["JUMP"] == ins:
			
			pass
		elif opcodes["SKIPCOND"] == ins:
			
			pass
		elif opcodes["JNS"] == ins:
			
			pass
		elif opcodes["JUMPI"] == ins:
			
			pass
		elif opcodes["STOREI"] == ins:
			
			pass
		elif opcodes["LOADI"] == ins:
			
			pass
		elif opcodes["HALT"] == ins:
			
			raise StopIteration
			
			
		
		self.PC.setDec(self.PC.getDec() + 1)
			
		
		
		
		

		
e = Emulator(fileName = "test.txt")
x = 0
for i in e:
	x += 1
print("finished program excecution")
