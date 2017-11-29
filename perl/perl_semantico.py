# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 01:54:01 2017

@author: Gustavo
"""

txt = " "
cont = 0

def incrementarContador():
    global cont
    cont +=1
    return "%d" %cont
    
class Nodo():
    pass

class Null(Nodo):
	def __init__(self):
		self.type = 'void'

	def imprimir(self,ident):
		print ident + "nodo nulo"

	def traducir(self):
		global txt
		id = incremetarContador()
		txt += id+"[label= "+"nodo_nulo"+"]"+"\n\t"

		return id

class program(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.name = hijo1

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)
		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		hijo1 = self.hijo1.traducir()

		txt += id +"[label= "+self.name+"]"+"\n\t"
		txt += id +"->"+hijo1+"\n\t"

		return "digraph G {\n\t"+txt+"}"

class declaration_list_1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id

class declaration_list_2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id

class p_declaration1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_declaration2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_declaration3(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_declaration4(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_header_declaration_1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_var_declaration_1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_var_declaration_2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_var_declaration_3(Nodo):
def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id


class p_var_declaration_4(Nodo):
def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id


class p_var_declaration_5(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_var_declaration_6(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_var_declaration_7(Nodo):
def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id


class p_var_declaration_8(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_var_declaration_9(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_var_declaration_10(Nodo):
def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id


class p_var_declaration_11(Nodo):
def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id


class p_var_declaration_12(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_var_declaration_13(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_var_declaration_14(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_var_declaration_15(Nodo):
def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id


class p_var_declaration_16(Nodo):
def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id


class p_fun_execute1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_fun_execute2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_fun_execute3(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_fun_declaration(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_params_1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_param_list_1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_param_list_2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_param_list_3(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_param_1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_param_2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_compount_stmt1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_compount_stmt2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_compount_stmt3(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_local_declarations_1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_local_declarations_2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_statement_list_1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_statement_list_2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_statement1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_statement2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_statement3(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_statement4(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_statement5(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_expression_stmt_1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_expression_stmt_2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_selection_stmt_1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_selection_stmt_2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_selection_stmt_3(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_iteration_stmt_1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_iteration_stmt_2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_return_stmt_1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_return_stmt_2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_expression_1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_expression_2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_expression_3(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_var_1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_var_2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_var_3(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_simple_expression_1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_simple_expression_2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_relop1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_relop2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_relop3(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_relop4(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_relop5(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_relop6(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_relop7(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_relop8(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_additive_expression_1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_additive_expression_2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_additive_expression_3(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_additive_expression_4(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_additive_expression_5(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_additive_expression_6(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_additive_expression_7(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_additive_expression_8(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_addop1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_addop2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_term_1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_term_2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_mulop1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_mulop2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_factor_1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_factor_2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_factor_3(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_factor_4(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_call(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_args1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_args2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_args_list_1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_args_list_2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class p_empty(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		
