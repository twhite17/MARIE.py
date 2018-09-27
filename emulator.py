

import convert

class Memory:
	
	def __init__(self):
		self.data = [[[0 for i in range(16)] for i2 in range(16)] for i in range(16)]
	
	def print(self, form="dec"):
		
		sect = ""
		
		
		for x in self.data:
			
			block = ""
			
			for y in x:
				
				row = ""
				
				for z in y:
					
					row += " "+str(convert.decToHex(z))+" "
				
				block += row + "\n"
		
			sect += block + "\n" +("-"*82)+ "\n"
			
		print(sect)
	
	def getAddr(self, addr):
		pass
	
	def setAddr(self, addr, val):
		pass
		

class Emulator:
	
	def __init__(self, inp = None, fileName=None):
		assert not (inp == None and fileName == None), AssertionError("One of inp or fileName must be non Nonetype.")
		self.memory = Memory()
		self.AC = 0
		self.IR = 0
		self.MAR = 0
		self.MBR = 0
		self.PC = 0
		self.IN = 0
		self.OUT = 0
		
		
	def __iter__(self):
		self.line = 0
		return self
	
	def __next__(self):
		r = self.run()
		return r
		
	def run(self):
		
		
		
		
		self.line += 1
		return True
		

		
e = Emulator(inp = "heiuof")		