import ply.yacc as yacc
from cal_lexer import tokens
import cal_lexer
import sys

VERBOSE = 1






def p_expresion_1(p):
	'expresion_est : expresion_est SEMICOLON'
	pass

#def p_expresion_2(p):
#	'expresion_est : SEMICOLON'
#	pass


def p_expresion(p):
		'''expresion : expresion SUMA termino 
                          | expresion RESTA termino 
                          | termino'''
pass

def p_termino(p):
		'''termino : termino MULTIPLICACION factor	
                          | termino DIVISION factor
                          | factor'''
pass

def p_factor(p):
		'''factor : PARDER expresion PARIZQ 
                          | IDEN 
                          | NUM'''
pass



def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(cal_lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')
		

parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba.cal'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("Tu parser reconocio correctamente todo")
	#input()
