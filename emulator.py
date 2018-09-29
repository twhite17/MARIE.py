

import convert
from numpy import int16
from numpy import array

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

def loadHex(val):
	
	val = val.lower()
	
	
	

class Memory:
	
	def __init__(self):
		self.data = array([int16(0) for i in range(2**12)])
	
	def loadAddr(self, addr):
		if addr < 0:
			addr += 0x10000
		return self.data[addr]
	
	def storeAddr(self, addr, val):
		if addr < 0:
			addr += 0x10000
		self.data[addr] = val
	
		

class Emulator:
	
	def __init__(self, inp = None, fileName=None):
		#assert not (inp == None and fileName == None), AssertionError("One of inp or fileName must be non Nonetype.")
		self.memory = Memory()
		self.AC 	= int16(0)
		self.IR 	= int16(0)
		self.MAR 	= int16(0)
		self.MBR 	= int16(0)
		self.PC 	= int16(0)
		self.IN 	= int16(0)
		self.OUT 	= int16(0)
		
		if inp == None:
			f = open(fileName, "r")
			c = f.read()
			c = c.split("\n")
			self.loadProgram(c)
			
		elif fileName == None:
			self.loadProgram(inp)
		
		#self.memory.print()
	
	def loadProgram(self, data):
		
		for index in range(len(data)):
			self.memory.storeAddr(index, int16(int(data[index], 16)))
			
		
	def __iter__(self):
		self.PC = int16(0)
		self.n = 0
		return self
	
	def __next__(self):
		
		#print(self.memory.loadAddr(self.PC.getHex()))
		#print(self.PC)
		self.IR = self.memory.loadAddr(self.PC)
		#print(self.IR.getHex())
		
		
		tmp = convert.decToHex(self.IR, 4)
		
		if self.n < 30:
			self.n += 1
			#print(convert.decToHex(self.IR, 4), int(tmp[1:], 16))
		
		
		
		ins = tmp[0]
		X = int16(int(tmp[1:], 16))
		
		#print(ins)
		
		if opcodes["ADD"] == ins:
			self.MAR = X
			self.MBR = self.memory.loadAddr(self.MAR)
			self.AC = self.AC + self.MBR
			
			
			
		elif opcodes["SUBT"] == ins:
			self.MAR = X
			self.MBR = self.memory.loadAddr(self.MAR)
			self.AC = self.AC - self.MBR
			
		elif opcodes["ADDI"] == ins:
			self.MAR = X
			self.MBR = self.memory.loadAddr(self.MAR)
			self.MAR = self.MBR
			self.MBR = self.memory.loadAddr(self.MAR)
			self.AC = self.AC + self.MBR
			
			
		elif opcodes["CLEAR"] == ins:
			self.AC = int16(0)
			
		elif opcodes["LOAD"] == ins:
			self.MAR = X
			self.MBR = self.memory.loadAddr(self.MAR)
			self.AC = self.MBR
			
		elif opcodes["STORE"] == ins:
			self.MAR = X
			self.MBR = self.AC
			self.memory.storeAddr(self.MAR, self.AC)
			
		elif opcodes["INPUT"] == ins:
			
			pass
		elif opcodes["OUTPUT"] == ins:
			print(self.AC)
			
		elif opcodes["JUMP"] == ins:
			self.PC = X - 1
			
		elif opcodes["SKIPCOND"] == ins:
			if X == 0x000:
				if self.AC < 0:
					self.PC += 1
			elif X == 0x400:
				if self.AC == 0:
					self.PC += 1
			elif X == 0x800:
				if self.AC > 0:
					self.PC += 1
			
		elif opcodes["JNS"] == ins:
			self.MAR = X
			self.MBR = self.PC
			self.memory.storeAddr(self.MAR, self.MBR)
			self.AC = X
			self.PC = self.AC
			
		elif opcodes["JUMPI"] == ins:
			self.MAR = X
			self.MBR = self.memory.loadAddr(self.MAR)
			self.MAR = self.MBR
			#print(self.MAR)
			#self.MBR = self.memory.loadAddr(self.MAR)
			#print(self.PC)

			self.PC = self.MBR
			
		elif opcodes["STOREI"] == ins:
			self.MAR = X
			self.MBR = self.memory.loadAddr(self.MAR)
			self.MAR = self.MBR
			self.memory.storeAddr(self.MAR, self.AC)
			
		elif opcodes["LOADI"] == ins:
			self.MAR = X
			self.MBR = self.memory.loadAddr(self.MAR)
			self.MAR = self.MBR
			self.MBR = self.memory.loadAddr(self.MAR)
			self.AC = self.MBR
			
		elif opcodes["HALT"] == ins:
			
			raise StopIteration
			
			
		
		self.PC += 1
			
		
		
		
		

		
e = Emulator(fileName = "test.txt")
x = 0
for i in e:
	x += 1
print("finished program excecution")
