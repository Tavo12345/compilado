# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 14:33:58 2017

@author: Gustavo
"""


import ply.lex as lex
import sys

# list of tokens
tokens = (
    # Reserverd words
    
    #Cabecera
    'CABECERA',
    
    #Control 1
    'DO',
    'WHILE',
    'FOR',
    'FOREACH',
    'CONTINUE',
    
    #Control 2
    'IF',
    'ELSE',
    'ELSIF',
    'UNLESS',
    'UNTIL',
    
    #Control 3
    'GOTO',
    'NEXT',
    'LAST',
    'REDO',
    'RETURN',
    
    #Operadores
    'SUMA',
    'SUMASUMA',
    'RESTA',
    'RESTARESTA',
    'MULTIPLICA',
    'MULTIPLICAMULTIPLICA',
    'DIVIDE',
    'DIFERENTE',
    'COMPLEMENTO',
    'MAYOR',
    'MENOR',
    'IGUAL',
    'PUNTO',
    'RESTAMAYOR',
    'IGUALCOMPLEMENTO',
    'DIFERENTECOMPLEMENTO',
    'PORCENTAJE',
    'X',
    'MENORMENOR',
    'MAYORMAYOR',
    'MENORIGUAL',
    'MAYORIGUAL',
    'LT',
    'GT',
    'LE',
    'GE',
    'IGUALIGUAL',
    'DIFERENTEIGUAL',
    'MENORIGUALMAYOR',
    'EQ',
    'NE',
    'CMP',
    'AMPERSANT',
    'PLECA',
    'CARET',
    'AMPERSANTAMPERSANT',
    'PLECAPLECA',
    'PUNTOPUNTO',
    'PUNTOPUNTOPUNTO',
    'INTERROGACOLON',
    'SUMAIGUAL',
    'RESTAIGUAL',
    'MULTIPLICAIGUAL',
    'COMA',
    'IGUALMAYOR',
    'NOT',
    'AND',
    'OR',
    'XOR',
    
    #Identificadores
    'ABS',
    'CHMOD',
    'CHOP',
    'CHOWN',
    'DEFINED',
    'DELETE',
    'DIE',
    'EOF',
    'EXIT',
    'EXP',
    'FILENO',
    'FORK',
    'HEX',
    'INT',
    'LC',
    'OCT',
    'REVERSE',
    'SEX',
    'RINDEX',
    'SPRINTF',
    'SUBSTR',
    'TRDIAGONAL',
    'PRINT',
    'UC',
    'UCFIRST',
    'YDIAGONAL',
    'QQDIAGONALSTRINGDIAGONAL',
    'ORD',
    'INDEX',
    'QDIAGONALSTRINGDIAGONAL',
    'LENGTH',
    'CRYPT',
    'CHR',
    'M',
    'POST',
    'SDIAGONAL',
    'STUDY',
    'LOG',
    'SIN',
    'EACH',
    
           
   
    #Simbolos    
    'SEMICOLON',    
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',    
    'HASHTAG',
    'SALTOLINEA',
    #'COMILLAS',

    # Others   
    'ID', 
    'NUMERO',
    #'PALABRA',
    'TEXTO',
)

# Regular expressions rules for a simple tokens 
t_SUMA   = r'\+'
t_RESTA  = r'-'
t_MULTIPLICA  = r'\*'
t_DIVIDE = r'/'
t_IGUAL  = r'='
t_DIFERENTE = r'!'
t_MENOR   = r'<'
t_MAYOR = r'>'
t_SEMICOLON = ';'
t_COMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_COLON   = r':'
t_AMPERSANT = r'\&'
t_PLECA = r'\|'
t_CARET = r'\^'
t_COMPLEMENTO = r'~'
t_HASHTAG = r'\#'
t_PUNTO = r'\.'
t_PORCENTAJE = r'\%'
t_SALTOLINEA = r'\\n'
#t_COMILLAS = r'"'

def t_CABECERA(t):
    r'\#\!/usr/bin/perl'
    return t

def t_DO(t):
    r'do'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_FOR(t):
    r'for'
    return t
    
def t_FOREACH(t):
    r'foreach'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_IF(t):
    r'if'
    return t


def t_ELSE(t):
    r'else'
    return t
    
def t_ELSIF(t):
    r'elsif'
    return t
    
def t_UNLESS(t):
    r'unless'
    return t
    
def t_UNTIL(t):
    r'until'
    return t

def t_GOTO(t):
    r'goto'
    return t

def t_NEXT(t):
    r'next'
    return t

def t_LAST(t):
    r'last'
    return t

def t_REDO(t):
    r'redo'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_ABS(t):
    r'abs'
    return t

def t_CHMOD(t):
    r'chmod'
    return t

def t_CHOP(t):
    r'chop'
    return t

def t_CHOWN(t):
    r'chown'
    return t
    
def t_DEFINED(t):
    r'defined'
    return t
    
def t_DELETE(t):
    r'delete'
    return t
    
def t_DIE(t):
    r'die'
    return t
    
def t_EOF(t):
    r'eof'
    return t
    
def t_EXIT(t):
    r'exit'
    return t
    
def t_EXP(t):
    r'exp'
    return t
    
def t_FILENO(t):
    r'fileno'
    return t
    
def t_FORK(t):
    r'fork'
    return t
    
def t_HEX(t):
    r'hex'
    return t
    
def t_INT(t):
	r'int'
	return t
 
def t_LC(t):
    r'lc'
    return t
    
def t_OCT(t):
    r'oct'
    return t
    
def t_REVERSE(t):
    r'reverse'
    return t
    
def t_SEX(t):
    r'sex'
    return t
    
def t_RINDEX(t):
    r'rindex'
    return t
    
def t_SPRINTF(t):
    r'sprintf'
    return t
 
def t_SUBSTR(t):
    r'substr'
    return t
    
def t_TRDIAGONAL(t):
    r'tr/'
    return t
    
def t_PRINT(t):
    r'print'
    return t
    
def t_UC(t):
    r'uc'
    return t
    
def t_UCFIRST(t):
    r'ucfirst'
    return t

def t_YDIAGONAL(t):
    r'y/'
    return t
    
def t_QQDIAGONALSTRINGDIAGONAL(t):
    r'qq/string/'
    return t
    
def t_ORD(t):
    r'ord'
    return t
    
def t_INDEX(t):
    r'index'
    return t
    
def t_QDIAGONALSTRINGDIAGONAL(t):
    r'q/string/'
    return t
    
def t_LENGTH(t):
    r'length'
    return t
    
def t_CRYPT(t):
    r'crypt'
    return t
    
def t_CHR(t):
    r'chr'
    return t
    
def t_M(t):
    r'm'
    return t
    
def t_POST(t):
    r'post'
    return t
    
def t_SDIAGONAL(t):
    r's/'
    return t
    
def t_STUDY(t):
    r'study'
    return t
    
def t_LOG(t):
    r'log'
    return t
    
def t_SIN(t):
    r'sin'
    return t
    
def t_EACH(t):
    r'each'
    return t
    
def t_X(t):
    r'x'
    return t
    
def t_LT(t):
    r'lt'
    return t
 
def t_GT(t):
    r'gt'
    return t
    
def t_LE(t):
    r'le'
    return t
    
def t_GE(t):
    r'ge'
    return t
    
def t_EQ(t):
    r'eq'
    return t
    
def t_NE(t):
    r'ne'
    return t
    
def t_CMP(t):
    r'cmp'
    return t 

def t_NOT(t):
    r'not'
    return t

def t_AND(t):
    r'and'
    return t

def t_OR(t):
    r'or'
    return t

def t_XOR(t):
    r'xor'
    return t        

def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'(\$|@|%)\w+(_\d\w)*'
    return t
    
def t_TEXTO(t):
    r'\"\w+([\40-\176]+)?\"'
    return t
    
def t_SUMASUMA(t):
	r'\+\+'
	return t
 
def t_RESTARESTA(t):
	r'--'
	return t
 
def t_MULTIPLICAMULTIPLICA(t):
	r'\*\*'
	return t
 
def t_RESTAMAYOR(t):
	r'->'
	return t
    
def t_IGUALCOMPLEMENTO(t):
	r'=~'
	return t
 
def t_DIFERENTECOMPLEMENTO(t):
	r'!~'
	return t
 
def t_MENORMENOR(t):
	r'<<'
	return t
 
def t_MAYORMAYOR(t):
	r'>>'
	return t
 
def t_MENORIGUAL(t):
	r'<='
	return t
 
def t_MAYORIGUAL(t):
	r'>='
	return t
 
def t_IGUALIGUAL(t):
	r'=='
	return t
 
def t_DIFERENTEIGUAL(t):
	r'!='
	return t
 
def t_MENORIGUALMAYOR(t):
	r'<=>'
	return t
 
def t_AMPERSANTAMPERSANT(t):
	r'\&\&'
	return t
 
def t_PLECAPLECA(t):
	r'\|\|'
	return t
 
def t_PUNTOPUNTO(t):
	r'\.\.'
	return t
 
def t_PUNTOPUNTOPUNTO(t):
	r'\.\.\.'
	return t
 
def t_INTERROGACOLON(t):
	r'\?:'
	return t
 
def t_SUMAIGUAL(t):
	r'\+='
	return t
 
def t_RESTAIGUAL(t):
	r'-='
	return t
 
def t_MULTIPLICAIGUAL(t):
	r'\*='
	return t
 
def t_IGUALMAYOR(t):
	r'=<'
	return t
 
 
    
##########################################

    




def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_comments_C99(t):
    r'\#(.)*?\n'
    t.lexer.lineno += 1

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)
    
def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

 
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba.pl'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()

