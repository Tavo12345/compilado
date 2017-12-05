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
		print (ident + "nodo nulo")

	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id+"[label= "+"nodo_nulo"+"]"+"\n\t"

		return id

class program(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(self,ident):
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
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2          

	def imprimir(self,ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		if type(self.hijo1) == type(tuple()):
			hijo1 = self.hijo1[0].traducir()
		else:
			hijo1 = self.hijo1.traducir()

		if type(self.hijo2) == type(tuple()):
			hijo2 = self.hijo2[0].traducir()
		else:
			hijo2 = self.hijo2.traducir()


		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id

class declaration_list_2(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(self,ident):
		self.hijo1.imprimir(" "+ident)
		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		if type(self.hijo1) == type(tuple()):
			hijo1 = self.hijo1[0].traducir()
		else:
			hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id

class declaration1(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(self,ident):
		self.hijo1.imprimir(" "+ident)
		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		if type(self.hijo1) == type(tuple()):
			hijo1 = self.hijo1[0].traducir()
		else:
			hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class declaration2(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo = hijo1

	def imprimir(self,ident):
		self.hijo1.imprimir(" "+ident)
		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()
		if type(self.hijo1) == type(tuple()):
			hijo1 = self.hijo1[0].traducir()
		else:
			hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class declaration3(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(self,ident):
		self.hijo1.imprimir(" "+ident)
		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		if type(self.hijo1) == type(tuple()):
			hijo1 = self.hijo1[0].traducir()
		else:
			hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class declaration4(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(self,ident):
		self.hijo1.imprimir(" "+ident)
		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		if type(self.hijo1) == type(tuple()):
			hijo1 = self.hijo1[0].traducir()
		else:
			hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class header_declaration_1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(ident):
         print (ident + "Cabecera")

	def traducir(self):
		global txt
		id = incrementarContador()

		return id
		

class var_declaration_1(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(self,ident):
		self.hijo1.imprimir(" "+ident)
		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		if type(self.hijo1) == type(tuple()):
			hijo1 = self.hijo1[0].traducir()
		else:
			hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class var_declaration_2(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)
		self.hijo2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id
		

class var_declaration_3(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)
		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id


class var_declaration_4(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)		

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id


class var_declaration_5(Nodo):
	def __init__(self,hijo1,hijo2,hijo3,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2
		self.hijo3 = hijo3

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)
		self.hijo2.imprimir(" "+ident)
		if type(self.hijo3) == type(tuple()):
			self.hijo3[0].imprimir(" "+ident)
		else:
			self.hijo3.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()
		hijo3 = self.hijo3.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"
		txt += id + " -> " + hijo3 + "\n\t"

		return id
		

class var_declaration_6(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)
		self.hijo2.imprimir(" "+ident)	

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()
		
		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id
		

class var_declaration_7(Nodo):
	def __init__(self,hijo1,hijo2,hijo3,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2
		self.hijo3 = hijo3

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)
		self.hijo2.imprimir(" "+ident)
		if type(self.hijo3) == type(tuple()):
			self.hijo3[0].imprimir(" "+ident)
		else:
			self.hijo3.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()
		hijo3 = self.hijo3.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"
		txt += id + " -> " + hijo3 + "\n\t"

		return id


class var_declaration_8(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)
		self.hijo2.imprimir(" "+ident)
		
		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id
		

class var_declaration_9(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)
		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id
		

class var_declaration_10(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)
		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id


class var_declaration_11(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)
		self.hijo2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id


class var_declaration_12(Nodo):
	def __init__(self,hijo1,hijo2,hijo3,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2
		self.hijo3 = hijo3

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)
		self.hijo2.imprimir(" "+ident)
		if type(self.hijo3) == type(tuple()):
			self.hijo3[0].imprimir(" "+ident)
		else:
			self.hijo3.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()
		hijo3 = self.hijo3.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"
		txt += id + " -> " + hijo3 + "\n\t"

		return id
		

class var_declaration_13(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)
		
		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

#class var_declaration_14(Nodo):
#	def __init__(self,name):
#		self.name = name
#
#	def imprimir(ident):
#
#	def traducir(self):
#		global txt
#		id = incrementarContador()
#
#		return id
		

class var_declaration_15(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id


class var_declaration_16(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)
		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id


class fun_execute1(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)
		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id
		

class fun_execute2(Nodo):
	def __init__(self,hijo1,hijo2,hijo3,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2
		self.hijo3 = hijo3

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)
		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		if type(self.hijo3) == type(tuple()):
			self.hijo3[0].imprimir(" "+ident)
		else:
			self.hijo3.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()
		hijo3 = self.hijo3.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"
		txt += id + " -> " + hijo3 + "\n\t"

		return id
		

class fun_execute3(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)
		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id
		

class fun_declaration(Nodo):
	def __init__(self,hijo1,hijo2,hijo3,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2
		self.hijo3 = hijo3

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)
		self.hijo2.imprimir(" "+ident)
		if type(self.hijo3) == type(tuple()):
			self.hijo3[0].imprimir(" "+ident)
		else:
			self.hijo3.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()
		hijo3 = self.hijo3.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"
		txt += id + " -> " + hijo3 + "\n\t"

		return id
		

class params_1(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class param_list_1(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id
		

class param_list_2(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

#class param_list_3(Nodo):
#	def __init__(self,name):
#		self.name = name
#
#	def imprimir(ident):
#
#	def traducir(self):
#		global txt
#		id = incrementarContador()
#
#		return id
		

class param_1(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class param_2(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class compount_stmt1(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class compount_stmt2(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class compount_stmt3(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class local_declarations_1(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id
		

#class local_declarations_2(Nodo):
#	def __init__(self,name):
#		self.name = name
#
#	def imprimir(ident):
#
#	def traducir(self):
#		global txt
#		id = incrementarContador()
#
#		return id
		

class statement_list_1(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id
		

#class statement_list_2(Nodo):
#	def __init__(self,name):
#		self.name = name
#
#	def imprimir(ident):
#
#	def traducir(self):
#		global txt
#		id = incrementarContador()
#
#		return id
		

class statement1(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class statement2(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class statement3(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class statement4(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class statement5(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class expression_stmt_1(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

#class expression_stmt_2(Nodo):
#	def __init__(self,name):
#		self.name = name
#
#	def imprimir(ident):
#
#	def traducir(self):
#		global txt
#		id = incrementarContador()
#
#		return id
		

class selection_stmt_1(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id
		

class selection_stmt_2(Nodo):
	def __init__(self,hijo1,hijo2,hijo3,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2
		self.hijo3 = hijo3

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		if type(self.hijo3) == type(tuple()):
			self.hijo3[0].imprimir(" "+ident)
		else:
			self.hijo3.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()		
		hijo3 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"
		txt += id + " -> " + hijo3 + "\n\t"

		return id
		

class selection_stmt_3(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id
		

class iteration_stmt_1(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id
		

class iteration_stmt_2(Nodo):
	def __init__(self,hijo1,hijo2,hijo3,hijo4,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2
		self.hijo3 = hijo3
		self.hijo4 = hijo4

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		if type(self.hijo3) == type(tuple()):
			self.hijo3[0].imprimir(" "+ident)
		else:
			self.hijo3.imprimir(" "+ident)

		if type(self.hijo4) == type(tuple()):
			self.hijo4[0].imprimir(" "+ident)
		else:
			self.hijo4.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()
		hijo3 = self.hijo3.traducir()
		hijo4 = self.hijo4.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"
		txt += id + " -> " + hijo3 + "\n\t"
		txt += id + " -> " + hijo4 + "\n\t"

		return id
		

class return_stmt_1(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class return_stmt_2(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)

		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id
		

class expression_1(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id
		

class expression_2(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class expression_3(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		self.hijo2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id
		

class var_1(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class var_2(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class var_3(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)

		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id
		

class simple_expression_1(Nodo):
	def __init__(self,hijo1,hijo2,hijo3,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2
		self.hijo3 = hijo3

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		if type(self.hijo3) == type(tuple()):
			self.hijo3[0].imprimir(" "+ident)
		else:
			self.hijo3.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()
		hijo3 = self.hijo3.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"
		txt += id + " -> " + hijo3 + "\n\t"

		return id
		

class simple_expression_2(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

#class relop1(Nodo):
#	def __init__(self,name):
#		self.name = name
#
#	def imprimir(ident):
#
#	def traducir(self):
#		global txt
#		id = incrementarContador()
#
#		return id
#		
#
#class relop2(Nodo):
#	def __init__(self,name):
#		self.name = name
#
#	def imprimir(ident):
#
#	def traducir(self):
#		global txt
#		id = incrementarContador()
#
#		return id
#		
#
#class relop3(Nodo):
#	def __init__(self,name):
#		self.name = name
#
#	def imprimir(ident):
#
#	def traducir(self):
#		global txt
#		id = incrementarContador()
#
#		return id
		

#class relop4(Nodo):
#	def __init__(self,name):
#		self.name = name
#
#	def imprimir(ident):
#
#	def traducir(self):
#		global txt
#		id = incrementarContador()
#
#		return id
#		
#
#class relop5(Nodo):
#	def __init__(self,name):
#		self.name = name
#
#	def imprimir(ident):
#
#	def traducir(self):
#		global txt
#		id = incrementarContador()
#
#		return id
		

#class relop6(Nodo):
#	def __init__(self,name):
#		self.name = name
#
#	def imprimir(ident):
#
#	def traducir(self):
#		global txt
#		id = incrementarContador()
#
#		return id
		

#class relop7(Nodo):
#	def __init__(self,name):
#		self.name = name
#
#	def imprimir(ident):
#
#	def traducir(self):
#		global txt
#		id = incrementarContador()
#
#		return id
		

#class relop8(Nodo):
#	def __init__(self,name):
#		self.name = name
#
#	def imprimir(ident):
#
#	def traducir(self):
#		global txt
#		id = incrementarContador()
#
#		return id
		

class additive_expression_1(Nodo):
	def __init__(self,hijo1,hijo2,hijo3,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2
		self.hijo3 = hijo3

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		if type(self.hijo3) == type(tuple()):
			self.hijo3[0].imprimir(" "+ident)
		else:
			self.hijo3.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()
		hijo3 = self.hijo3.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"
		txt += id + " -> " + hijo3 + "\n\t"

		return id
		

class additive_expression_2(Nodo):
	def __init__(self,hijo1,hijo2,hijo3,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2
		self.hijo3 = hijo3

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		if type(self.hijo3) == type(tuple()):
			self.hijo3[0].imprimir(" "+ident)
		else:
			self.hijo3.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()
		hijo3 = self.hijo3.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"
		txt += id + " -> " + hijo3 + "\n\t"

		return id
		

class additive_expression_3(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class additive_expression_4(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class additive_expression_5(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class additive_expression_6(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class additive_expression_7(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class additive_expression_8(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class addop1(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print (ident+" + ")
			
	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id + "[label= "+str(self.name)+"]"+"\n\t"

		return id
		

class addop2(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print (ident+" - ")
			
	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id + "[label= "+str(self.name)+"]"+"\n\t"

		return id
		

class term_1(Nodo):
	def __init__(self,hijo1,hijo2,hijo3,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2
		self.hijo3 = hijo3

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		if type(self.hijo3) == type(tuple()):
			self.hijo3[0].imprimir(" "+ident)
		else:
			self.hijo3.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()
		hijo3 = self.hijo3.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"
		txt += id + " -> " + hijo3 + "\n\t"

		return id
		

class term_2(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class mulop1(Nodo):
	def __init__(self,name):
              self.name = name

	def imprimir(self,ident):
		print (ident+" * ")
			
	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id + "[label= "+str(self.name)+"]"+"\n\t"

		return id
#		

class mulop2(Nodo):
	def __init__(self,name):
              self.name = name

	def imprimir(self,ident):
		print (ident+" / ")
			
	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id + "[label= "+str(self.name)+"]"+"\n\t"

		return id
		

class factor_1(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class factor_2(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class factor_3(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class factor_4(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

class call(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		self.hijo1.imprimir(" "+ident)

		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id
		

class args1(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

#class args2(Nodo):
#	def __init__(self,name):
#		self.name = name
#
#	def imprimir(ident):
#
#	def traducir(self):
#		global txt
#		id = incrementarContador()
#
#		return id
		

class args_list_1(Nodo):
	def __init__(self,hijo1,hijo2,name):
		self.name = name
		self.hijo1 = hijo1
		self.hijo2 = hijo2

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		if type(self.hijo2) == type(tuple()):
			self.hijo2[0].imprimir(" "+ident)
		else:
			self.hijo2.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()
		hijo2 = self.hijo2.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"
		txt += id + " -> " + hijo2 + "\n\t"

		return id
		

class args_list_2(Nodo):
	def __init__(self,hijo1,name):
		self.name = name
		self.hijo1 = hijo1

	def imprimir(ident):
		if type(self.hijo1) == type(tuple()):
			self.hijo1[0].imprimir(" "+ident)
		else:
			self.hijo1.imprimir(" "+ident)

		print (ident + "Nodo: "+self.name)

	def traducir(self):
		global txt
		id = incrementarContador()

		hijo1 = self.hijo1.traducir()

		txt += id + "[label= "+self.name+"]"+"\n\t"
		txt += id + " -> " + hijo1 + "\n\t"

		return id
		

#class empty(Nodo):
#	def __init__(self,name):
#		self.name = name
#
#	def imprimir(ident):
#
#	def traducir(self):
#		global txt
#		id = incrementarContador()
#
#		return id
		



class Id(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print (ident+"ID: "+self.name)
			
	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id + "[label= "+self.name+"]"+"\n\t"

		return id

class Idf(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print (ident+"IDF: "+self.name)
			
	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id + "[label= "+self.name+"]"+"\n\t"

		return id

class Suma(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print (ident+"SUMA: "+self.name)
			
	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id + "[label= \""+self.name+"\"]"+"\n\t"

		return id

class Resta(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print (ident+"RESTA: "+self.name)
			
	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id + "[label= \""+self.name+"\"]"+"\n\t"

		return id

class Divide(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print (ident+"DIVIDE: "+self.name)
			
	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id + "[label= \""+self.name+"\"]"+"\n\t"

		return id

class Numero(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print (ident+"Numero: "+str(self.name))
			
	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id + "[label= "+str(self.name)+"]"+"\n\t"

		return id
  
class Texto(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print (ident+"Texto: "+str(self.name))
			
	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id + "[label= "+str(self.name)+"]"+"\n\t"

		return id
  
  
class Print(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print (ident+"Print: "+str(self.name))
			
	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id + "[label= "+str(self.name)+"]"+"\n\t"

		return id
  
  
class Chop(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print (ident+"Chop: "+str(self.name))
			
	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id + "[label= "+str(self.name)+"]"+"\n\t"

		return id
  
class Sub(Nodo):
	def __init__(self,name):
		self.name = name

	def imprimir(self,ident):
		print (ident+"Sub: "+str(self.name))
			
	def traducir(self):
		global txt
		id = incrementarContador()
		txt += id + "[label= "+str(self.name)+"]"+"\n\t"

		return id