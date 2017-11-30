# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 12:10:43 2017

@author: Gustavo
"""

import ply.yacc as yacc
import os
import codecs
import re
from perl_lexer import tokens
import perl_lexer
from sys import stdin
from perl_semantico import *

#VERBOSE = 1

precedence = (
	('right','ID','IDF','IF','WHILE','UNTIL','FOR'),
#	('right','PROCEDURE'),
	('right','VAR'),
#	('right', 'ASSIGN'),
#	('right','UPDATE'),
#	('left','NE'),
#	('left','LT','LTE','GT','GTE'),
	('left','SUMA','RESTA'),
	('left','MULTIPLICA','DIVIDE'),
#	('right','ODD'),
	('left','LPARENT','RPARENT'),
 )
	
 

def p_program(p):
	'program : declaration_list'
	p[0] = program(p[1],"program")	

def p_declaration_list_1(p):
	'declaration_list : declaration_list  declaration' 
	p[0] = declaration_list1(p[1],p[2],"declaration_list1")

def p_declaration_list_2(p):
	'declaration_list : declaration'
	p[0] = declaration_list2(p[1],"declaration_list2")

def p_declaration1(p):
	'''declaration : var_declaration'''
	p[0] = declaration1(p[1],"declaration1")

def p_declaration2(p):
	'''declaration : fun_declaration'''
	p[0] = declaration2(p[1],"declaration2")

def p_declaration3(p):
	'''declaration : fun_execute'''
	p[0] = declaration3(p[1],"declaration3")

def p_declaration4(p):
	'''declaration : header_declaration'''
	p[0] = declaration4(p[1],"declaration4")

def p_header_declaration_1(p):
	'header_declaration : CABECERA'
	pass

def p_var_declaration_1(p):
	'var_declaration : var_declaration3 SEMICOLON'
	p[0] = var_declaration1(p[1],"var_declaration1")

def p_var_declaration_2(p):
	'var_declaration2 :  ID LBRACKET NUMERO RBRACKET SEMICOLON'
	p[0] = declaration2(Id(p[1]),Numero(p[3]),"declaration2")

def p_var_declaration_3(p):                     
	'''var_declaration3 : ID COMA var_declaration2'''
	p[0] = declaration3(Id(p[1]),p[3],"declaration3")

def p_var_declaration_4(p):                     
	'''var_declaration3 : ID'''
	p[0] = declaration4(Id(p[1]),"declaration4")

def p_var_declaration_5(p):                     
	'''var_declaration3 : ID IGUAL NUMERO COMA var_declaration2'''
	p[0] = declaration5(Id(p[1]),Numero(p[3]),p[5],"declaration5")

def p_var_declaration_6(p):                     
	'''var_declaration3 : ID IGUAL NUMERO'''
	p[0] = declaration6(Id(p[1]),Numero(p[3]),"declaration6")

def p_var_declaration_7(p):                     
	'''var_declaration3 : ID IGUAL TEXTO COMA var_declaration2'''
	p[0] = declaration7(Id(p[1]),Texto(p[3]),p[5],"declaration7")

def p_var_declaration_8(p):                     
	'''var_declaration3 : ID IGUAL TEXTO'''
	p[0] = declaration8(Id(p[1]),Texto(p[3]),"declaration8")

def p_var_declaration_9(p):                     
	'''var_declaration3 : ID IGUAL simple_expression'''
	p[0] = declaration9(Id(p[1]),p[3],"declaration9")

def p_var_declaration_10(p):                     
	'''var_declaration3 : MULTIPLICA ID COMA var_declaration2'''
	p[0] = declaration10(Id(p[2]),p[4],"declaration10")

def p_var_declaration_11(p):                     
	'''var_declaration3 : ID IGUAL ID'''
	p[0] = declaration11(Id(p[1]),Id(p[3]),"declaration11")

def p_var_declaration_12(p):                     
	'''var_declaration3 : ID IGUAL ID COMA var_declaration2'''
	p[0] = declaration12(Id(p[1]),Id(p[3]),p[5],"declaration12")

def p_var_declaration_13(p):                     
	'''var_declaration3 : MULTIPLICA ID'''
	p[0] = declaration13(Id(p[2]),"declaration13")

def p_var_declaration_14(p):                     
	'''var_declaration3 : COMA'''
	pass

def p_var_declaration_15(p):                     
	'''var_declaration3 : MULTIPLICA MULTIPLICA ID'''
	p[0] = declaration15(Id(p[3]),"declaration15")

def p_var_declaration_16(p):                     
	'''var_declaration3 : MULTIPLICA MULTIPLICA ID COMA var_declaration2'''
	p[0] = declaration16(Id(p[3]),p[5],"declaration16")

def p_fun_execute1(p):
    '''fun_execute : PRINT expression SEMICOLON'''
    p[0] = fun_execute1(Print(p[1]),p[2],"fun_execute1")

def p_fun_execute2(p):
    '''fun_execute : PRINT expression COMA expression SEMICOLON'''
    p[0] = fun_execute2(Print(p[1]),p[2],p[4],"fun_execute2")

def p_fun_execute3(p):
    '''fun_execute : CHOP expression SEMICOLON'''
    p[0] = fun_execute3(Chop(p[1]),p[2],"fun_execute3")

def p_fun_declaration(p):
	'fun_declaration : SUB IDF LBLOCK compount_stmt RBLOCK'
	p[0] = fun_declaration(Sub(p[1]),Idf(p[2]),p[4],"fun_declaration")

def p_params_1(p):
	'params : param_list'
	p[0] = params_1(p[1],"params_1")

def p_param_list_1(p):
	'param_list : param_list COMA param'
	p[0] = params_list_1(p[1],p[3],"params_list_1")

def p_param_list_2(p):
	'param_list : param'
	p[0] = params_list_2(p[1],"params_list_2")

def p_param_list_3(p):
	'param_list : empty'
	p[0] = Null()

def p_param_1(p):
	'param : ID'
	p[0] = param_1(Id(p[1]),"param_1")

def p_param_2(p):
	'param :  ID LBRACKET RBRACKET'
	p[0] = param_2(Id(p[1]),"param_2")

def p_compount_stmt1(p):
	'''compount_stmt : var_declaration'''
	p[0] = compount_stmt1(p[1],"compount_stmt1")

def p_compount_stmt2(p):
	'''compount_stmt : fun_execute'''
	p[0] = compount_stmt2(p[1],"compount_stmt2")

def p_compount_stmt3(p):
	'''compount_stmt : header_declaration'''
	p[0] = compount_stmt3(p[1],"compount_stmt3")

def p_local_declarations_1(p):
	'local_declarations : local_declarations var_declaration'
	p[0] = local_declarations_1(p[1],p[2],"local_declarations_1")

def p_local_declarations_2(p):
	'local_declarations : empty'
	p[0] = Null()

def p_statement_list_1(p):
	'statement_list : statement_list statement'
	p[0] = statement_list_1(p[1],p[2],"statement_list_1")

def p_statement_list_2(p):
	'statement_list : empty'	
	p[0] = Null()

def p_statement1(p):
	'''statement : expression_stmt'''
	p[0] = statement1(p[1],"statement1") 

def p_statement2(p):
	'''statement : compount_stmt'''
	p[0] = statement2(p[1],"statement2")

def p_statement3(p):
	'''statement : selection_stmt'''
	p[0] = statement3(p[1],"statement3")

def p_statement4(p):
	'''statement : iteration_stm'''
	p[0] = statement4(p[1],"statement4")

def p_statement5(p):
	'''statement : return_stmt'''
	p[0] = statement5(p[1],"statement5")

def p_expression_stmt_1(p):
	'expression_stmt : expression SEMICOLON'
	p[0] = expression_stmt_1(p[1],"expression_stmt_1")

def p_expression_stmt_2(p):
	'expression_stmt : SEMICOLON'
	pass

def p_selection_stmt_1(p):
	'selection_stmt : IF LPAREN expression RPAREN statement'
	p[0] = selection_stmt_1(p[3],p[5],"selection_stmt_1")

def p_selection_stmt_2(p):
	'selection_stmt : IF LPAREN expression RPAREN statement ELSE statement'
	p[0] = selection_stmt_2(p[3],p[5],p[7],"selection_stmt_2")

def p_selection_stmt_3(p):
	'selection_stmt : UNTIL LPAREN expression RPAREN statement'
	p[0] = selection_stmt_3(p[3],p[5],"selection_stmt_3")

def p_iteration_stmt_1(p):
	'iteration_stmt : WHILE LPAREN expression RPAREN statement'
	p[0] = iteration_stmt_1(p[3],p[5],"iteration_stmt_1")

def p_iteration_stmt_2(p):
	'iteration_stmt : FOR LPAREN var_declaration2 SEMICOLON expression SEMICOLON additive_expression RPAREN statement'
	p[0] = iteration_stmt_2(p[3],p[5],p[7],p[9],"iteration_stmt_2")

def p_return_stmt_1(p):
	'return_stmt : RETURN SEMICOLON'
	p[0] = return_stmt_1(Return(p[1]),"return_stmt_1")

def p_return_stmt_2(p):
	'return_stmt : RETURN expression SEMICOLON'
	p[0] = return_stmt_2(Return(p[1]),p[2],"return_stmt_2")

def p_expression_1(p):
	'expression : var IGUAL expression'
	p[0] = expression_1(p[1],p[3],"expression_1")

def p_expression_2(p):
	'expression : simple_expression'
	p[0] = expression_2(p[1],"expression_2")

def p_expression_3(p):
	'expression : var IGUAL AMPERSANT ID'
	p[0] = expression_3(p[1],Id(p[4]),"expression_3")

def p_var_1(p):
	'''var : ID'''
	p[0] = var_1(Id(p[1]),"var_1")

def p_var_2(p):
	'''var : TEXTO'''
	p[0] = var_2(Texto(p[1]),"var_2")

def p_var_3(p):
	'var : ID LBRACKET expression RBRACKET'
	p[0] = var_3(Id(p[1]),p[3],"var_3")

def p_simple_expression_1(p):
	'simple_expression : additive_expression relop additive_expression'
	p[0] = simple_expression_1(p[1],p[2],p[3],"simple_expression_1")

def p_simple_expression_2(p):
	'simple_expression : additive_expression'
	p[0] = simple_expression_2(p[1],"simple_expression_2")


#def p_relop(p):
#	'''relop : MENOR 
#			| MENORIGUAL
#			| MAYOR
#			| MAYORIGUAL
#			| IGUAL
#			| DIFERENTE
#           | MENORIGUALMAYOR
#            | DIFERENTEIGUAL
#            | AMPERSANTAMPERSANT
#            | XOR
#            | AND
#            | OR
#            | NOT
#            | IGUALIGUAL
#            | RESTAMAYOR
#            | MAYORMAYOR
#            | MENORMENOR
#            | X
#            | LE
#            | LT
#            | GT
#            | EQ
#            | IGUALCOMPLEMENTO
#            | DIFERENTECOMPLEMENTO
#            | PORCENTAJE
#            | PUNTOPUNTOPUNTO
#            | IGUALMAYOR
#            | PLECAPLECA
#	'''
#	pass

def p_relop1(p):
	'''relop : MENOR'''
	pass

def p_relop2(p):
	'''relop : MAYOR'''
	pass

def p_relop3(p):
	'''relop : MENORIGUAL'''
	pass

def p_relop4(p):
	'''relop : MAYORIGUAL'''
	pass

def p_relop5(p):
	'''relop : IGUALIGUAL'''
	pass

def p_relop6(p):
	'''relop : DIFERENTEIGUAL'''
	pass

def p_relop7(p):
	'''relop : AND'''
	pass

def p_relop8(p):
	'''relop : OR'''
	pass

def p_additive_expression_1(p):
	'''additive_expression : additive_expression addop term'''
	p[0] = additive_expression_1(p[1],p[2],p[3],"additive_expression_1")

def p_additive_expression_2(p):
	'''additive_expression : additive_expression addop additive_expression'''
	p[0] = additive_expression_2(p[1],p[2],p[3],"additive_expression_2")

def p_additive_expression_3(p):
	'additive_expression : term'
	p[0] = additive_expression_3(p[1],"additive_expression_3")

def p_additive_expression_4(p):
	'additive_expression : term RESTARESTA'
	p[0] = additive_expression_4(p[1],"additive_expression_4")

def p_additive_expression_5(p):
	'additive_expression : term SUMASUMA'
	p[0] = additive_expression_5(p[1],"additive_expression_5")

def p_additive_expression_6(p):
	'additive_expression : term MULTIPLICAIGUAL'
	p[0] = additive_expression_6(p[1],"additive_expression_6")

def p_additive_expression_7(p):
	'additive_expression : term RESTAIGUAL'
	p[0] = additive_expression_7(p[1],"additive_expression_7")

def p_additive_expression_8(p):
	'additive_expression : term MULTIPLICAMULTIPLICA'
	p[0] = additive_expression_8(p[1],"additive_expression_8")

#def p_additive_expression_8(p):
#	'additive_expression : var'
#	pass

def p_addop1(p):
	'''addop : SUMA'''
	pass

def p_addop2(p):
	'''addop : RESTA'''
	pass

def p_term_1(p):
	'term : term mulop factor'
	p[0] = term_1(p[1],p[2],p[3],"term_1")

def p_term_2(p):
	'term : factor'
	p[0] = term_2(p[1],"term_2")



def p_mulop1(p):
	'''mulop : 	MULTIPLICA'''
	pass

def p_mulop2(p):
	'''mulop : DIVIDE'''
	pass

def p_factor_1(p):
	'factor : LPAREN expression RPAREN'
	p[0] = factor_1(p[2],"factor_1")

def p_factor_2(p):
	'factor : var'
	p[0] = factor_2(p[1],"factor_2")

def p_factor_3(p):
	'factor : call'
	p[0] = factor_3(p[1],"factor_3")

def p_factor_4(p):
	'factor : NUMERO' 
	p[0] = factor_4(Numero(p[2]),"factor_4")



def p_call(p):
	'call : ID LPAREN args RPAREN'
	p[0] = call(Id(p[1]),p[3],"call")

def p_args1(p):
	'''args : args_list'''
	p[0] = args1(p[1],"args1")

def p_args2(p):
	'''args : empty'''
	p[0] = Null()

def p_args_list_1(p):
	'args_list : args_list COMA expression'
	p[0] = args_list_1(p[1],p[3],"args_list_1")

def p_args_list_2(p):
	'args_list : expression'
	p[0] = args_list_2(p[1],"args_list_2")

def p_empty(p):
	'empty :'
	p[0] = Null()



#def p_error(p):
#	if VERBOSE:
#		if p is not None:
#			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
#		else:
#			print ("ERROR SINTACTICO EN LA LINEA: " + str(cminus_lexer.lexer.lineno))
#	else:
#		raise Exception('syntax', 'error')
		

#parser = yacc.yacc()


#if __name__ == '__main__':    
# #     print("hola")
#	if (len(sys.argv) > 1):
#		fin = sys.argv[1]
#	else:
#		fin = 'prueba.pl'

#	f = open(fin, 'r')
#	data = f.read()
#	#print (data)
#	parser.parse(data, tracking=True)
#	print("Tu parser reconocio correctamente todo")
#	#input()


def p_error(p):
	print ("Error de sintaxis ", p)
	#print "Error en la linea "+str(p.lineno)

def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print (str(cont)+". "+file)
		cont = cont+1

	while respuesta == False:
		numArchivo = input('\nNumero del test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print ("Has escogido \"%s\"" %files[int(numArchivo)-1])

	return files[int(numArchivo)-1]


def traducir(result):
	graphFile = open('graphviztrhee.vz','w')
	graphFile.write(result.traducir())
	graphFile.close()
	print ("El programa traducido se guardo en \"graphviztrhee.vz\"")
 

directorio = 'D:/UTP-2017-2/Compiladores/Proyecto/compilador/perl/test/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena,debug=1)

#result.imprimir(" ")
#print result.traducir()

#graphFile = open('graphviztrhee.vz','w')
#graphFile.write(result.traducir())
#graphFile.close() 


traducir(result)

#print (result)