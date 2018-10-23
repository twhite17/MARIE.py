from numpy import int16

decToHexData = {
	"10":"A",
	"11":"B",
	"12":"C",
	"13":"D",
	"14":"E",
	"15":"F"	
	}

hexToDecData = {
	"A":10,
	"B":11,
	"C":12,
	"D":13,
	"E":14,
	"F":15	
	}

def minHexLength(val, minLength):
	if len(val) < minLength:
		for i in range(minLength - len(val)):
			val = "0" + val
	return val

def isInteger(val):
	r = True
	try:
		x = int(val)	
	except:
		r = False
	return r

def _decToHex(val):
	assert val in range(0, 16), ValueError("ValueError, value must be in range 0 to 15 inclusive")
	if val <= 9:
		return str(val)
	else:
		return decToHexData[str(val)]
	

def decToHex(val, minLength=3): # note Hexadecimal values are stored as Strings
	r = ""
	if val < 0:
		val += 0x10000
	while val > 0:
		r = _decToHex(val % 16) + r
		val = val // 16
	if len(r) < minLength:
		for i in range(minLength-len(r)):
			r = "0"+r
	return r

def _hexToDec(val):
	if isInteger(val):
		return int(val)
	else:
		return hexToDecData[val]
	

def hexToDec(val):
	total = 0
	for ch in range(len(val)):
		total += _hexToDec(val[-(ch+1)]) * pow(16, ch)
	return total