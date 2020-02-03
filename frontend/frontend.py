from lexer import Lexer

fi = open("test.c","r")
toTokenize = fi.read()
fi.close()

lex = Lexer()
lex.setTokens()
tokens = lex.tokenize(toTokenize)
print(tokens)
