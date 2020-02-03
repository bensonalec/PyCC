import re

class Lexer:
	def __init__(self):
		self.regex = []
		self.names = []

	def setTokens(self):
		
		self.addReg([r"(auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while)", "KEYWORDS"])
		self.addReg([r"([a-zA-Z_]\w+\(|[a-zA-Z_]\()", "FUNCTION"])
		self.addReg([r"(\+|\-|\/|\*|\%)", "ARITHMETIC_OPERATOR"])
		self.addReg([r"(\d+)", "INTEGER"])
		self.addReg([r"(==|<=|>=|<|>)", "COMPARISON_OPERATOR"])
		self.addReg([r"(&&|\|\|)", "LOGIC_OPERATOR"])
		self.addReg([r"([a-zA-Z_]\w+|[a-zA-Z_])", "VARIABLE"])
		self.addReg([r"(\=)", "ASSIGNMENT"])
		self.addReg([r"(\()", "LEFT_PARENTHESES"])
		self.addReg([r"(\))", "RIGHT_PARENTHESES"])
		self.addReg([r"(\{)", "LEFT_BRACKET"])
		self.addReg([r"(\})", "RIGHT_BRACKET"])
		self.addReg([r"(\;)", "SEMICOLON"])
		
		self.finalizeRegex()
		
	def tokenize(self,toTokenize):
		output = re.compile(self.regex)
		tokens = []
		i = 0
		for group in output.findall(toTokenize):
			for match in group:
				if(match != ""):
					tokens.append([match,self.names[group.index(match)]])
			i += 1
		return tokens

	def addReg(self,regexPair):
		self.names.append(regexPair[1])
		self.regex.append(regexPair[0])

	def finalizeRegex(self):
		self.regex = '|'.join(self.regex)
