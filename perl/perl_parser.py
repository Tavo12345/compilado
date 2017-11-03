import ply.yacc as yacc
from perl_lexer import tokens
import perl_lexer
import sys

VERBOSE = 1

def p_program(p):
	'program : declaration_list'
	pass

def p_declaration_list_1(p):
	'declaration_list : declaration_list  declaration' 
	pass

def p_declaration_list_2(p):
	'declaration_list : declaration'
	pass

def p_declaration(p):
	'''declaration : var_declaration
				  | fun_declaration
				  | header_declaration'''
	pass

def p_header_declaration_1(p):
	'header_declaration : CABECERA'
	pass

def p_var_declaration_1(p):
	'var_declaration : var_declaration3 SEMICOLON'
	pass

def p_var_declaration_2(p):
	'var_declaration2 :  ID LBRACKET NUMERO RBRACKET SEMICOLON'
	pass

def p_var_declaration_3(p):                     
	'''var_declaration3 : ID COMA var_declaration2  
	                               | ID
	                               | ID IGUAL NUMERO COMA var_declaration2
	                               | ID IGUAL NUMERO
	                               | ID IGUAL TEXTO COMA var_declaration2
	                               | ID IGUAL TEXTO
	                               | MULTIPLICA ID COMA var_declaration2
	                               | MULTIPLICA ID
	                               | ID IGUAL ID COMA var_declaration2
	                               | ID IGUAL ID
	                               | COMA
	                               | MULTIPLICA MULTIPLICA ID
	                               | MULTIPLICA MULTIPLICA ID COMA var_declaration2

        '''
	pass


def p_fun_declaration(p):
	'fun_declaration : SUB ID LPAREN params RPAREN compount_stmt'
	pass

def p_params_1(p):
	'params : param_list'
	pass

def p_param_list_1(p):
	'param_list : param_list COMA param'
	pass

def p_param_list_2(p):
	'param_list : param'
	pass

def p_param_list_3(p):
	'param_list : empty'
	pass

def p_param_1(p):
	'param : ID'
	pass

def p_param_2(p):
	'param :  ID LBRACKET RBRACKET'
	pass

def p_compount_stmt(p):
	'compount_stmt : LBLOCK local_declarations statement_list RBLOCK'
	pass

def p_local_declarations_1(p):
	'local_declarations : local_declarations var_declaration'
	pass

def p_local_declarations_2(p):
	'local_declarations : empty'
	pass

def p_statement_list_1(p):
	'statement_list : statement_list statement'
	pass

def p_statement_list_2(p):
	'statement_list : empty'	
	pass

def p_statement(p):
	'''statement : expression_stmt
				| compount_stmt
				| selection_stmt
				| iteration_stmt
				| return_stmt
	'''
	pass

def p_expression_stmt_1(p):
	'expression_stmt : expression SEMICOLON'
	pass

def p_expression_stmt_2(p):
	'expression_stmt : SEMICOLON'
	pass

def p_selection_stmt_1(p):
	'selection_stmt : IF LPAREN expression RPAREN statement'
	pass

def p_selection_stmt_2(p):
	'selection_stmt : IF LPAREN expression RPAREN statement ELSE statement'
	pass

def p_iteration_stmt_1(p):
	'iteration_stmt : WHILE LPAREN expression RPAREN statement'
	pass



def p_iteration_stmt_2(p):
	'iteration_stmt : FOR LPAREN var_declaration2 SEMICOLON expression SEMICOLON additive_expression RPAREN statement'
	pass

def p_return_stmt_1(p):
	'return_stmt : RETURN SEMICOLON'
	pass

def p_return_stmt_2(p):
	'return_stmt : RETURN expression SEMICOLON'
	pass

def p_expression_1(p):
	'expression : var IGUAL expression'
	pass

def p_expression_2(p):
	'expression : simple_expression'
	pass

def p_expression_3(p):
	'expression : var IGUAL AMPERSANT ID'
	pass

def p_var_1(p):
	'var : ID'
	pass

def p_var_2(p):
	'var : ID LBRACKET expression RBRACKET'
	pass

def p_simple_expression_1(p):
	'simple_expression : additive_expression relop additive_expression'
	pass

def p_simple_expression_2(p):
	'simple_expression : additive_expression'
	pass


def p_relop(p):
	'''relop : MENOR 
			| MENORIGUAL
			| MAYOR
			| MAYORIGUAL
			| IGUAL
			| DIFERENTE
            | MENORIGUALMAYOR
            | DIFERENTEIGUAL
            | AMPERSANTAMPERSANT
            | XOR
            | AND
            | OR
            | NOT
            | IGUALIGUAL
            | RESTAMAYOR
            | MAYORMAYOR
            | MENORMENOR
            | X
            | LE
            | LT
            | GT
            | EQ
            | IGUALCOMPLEMENTO
            | DIFERENTECOMPLEMENTO
            | PORCENTAJE
            | PUNTOPUNTOPUNTO
            | IGUALMAYOR
            | PLECAPLECA
	'''
	pass

def p_additive_expression_1(p):
	'additive_expression : additive_expression addop term'
	pass

def p_additive_expression_2(p):
	'additive_expression : term'
	pass

def p_additive_expression_3(p):
	'additive_expression : term RESTARESTA'
	pass

def p_additive_expression_4(p):
	'additive_expression : term SUMASUMA'
	pass

def p_additive_expression_5(p):
	'additive_expression : term MULTIPLICAIGUAL'
	pass

def p_additive_expression_6(p):
	'additive_expression : term RESTAIGUAL'
	pass

def p_additive_expression_7(p):
	'additive_expression : term MULTIPLICAMULTIPLICA'
	pass


def p_addop(p):
	'''addop : SUMA 
				| RESTA 
	'''
	pass

def p_term_1(p):
	'term : term mulop factor'
	pass

def p_term_2(p):
	'term : factor'
	pass



def p_mulop(p):
	'''mulop : 	MULTIPLICA
				| DIVIDE
	'''
	pass

def p_factor_1(p):
	'factor : LPAREN expression RPAREN'
	pass

def p_factor_2(p):
	'factor : var'
	pass

def p_factor_3(p):
	'factor : call'
	pass

def p_factor_4(p):
	'factor : NUMERO' 
	pass



def p_call(p):
	'call : ID LPAREN args RPAREN'
	pass

def p_args(p):
	'''args : args_list
			| empty
	'''
	pass

def p_args_list_1(p):
	'args_list : args_list COMA expression'
	pass

def p_args_list_2(p):
	'args_list : expression'
	pass

def p_empty(p):
	'empty :'
	pass



def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(cminus_lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')
		

parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba.pl'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("Tu parser reconocio correctamente todo")
	#input()
