'''from collections import Counter

cadena1= input('ingrese primer una cadena de caracteres: ')
cadena2= input('ingrese segunda una cadena de caracteres: ')


cadena = 'texto'
Contador_1 = Counter(cadena1)
Contador_2 = Counter(cadena2)#Counter(cadena2)
#cadena = cadena1 & cadena2
print (list(cadena1), '\n')
print (list(cadena2), '\n')



print (cadena)
'''
#from new3 import repitencaracteres as rp


ListaUIDs=[]
ListaVal=[]
Mayus=[]
Minus=[]
Num=[]
CtdT=int(input('Ingrese la cantidad UID a validar:' ))

for i in range(CtdT):
	print  ('Ingrese el UID N°', i+1, 'por favor: ')
	ListaUIDs.append (input())
	minus,mayus,num=0,0,0
	texto=str(ListaUIDs[i])
	if len(texto)==10: #& texto.isalnum(): #& rp(texto)
		for c in texto:
			if c.isupper():
				mayus+=1
				Mayus.append(mayus)
			elif c.islower():
				minus+=1
				Minus.append(minus)
			elif c.isnumeric():
				num+=1
				Num.append(num)
		if mayus>1 & num>2:
			ListaVal.append('Valid')
			#else:
			#	ListaVal.append('Invalid')		
	else:
		ListaVal.append('Invalid')
else:
	for u in range(CtdT):
		print(ListaVal, Mayus.pop(), Minus.pop(), Num.pop())
	#print (Mayus.pop(),Minus.pop(),Num.pop())		 		
