
#Otávio Secco
#Vinicius dos Reis

def log():
	arq = open('teste03', 'r')
	texto = arq.readlines()
	arq.close()

	texto = [exclui.replace('\n', '') for exclui in texto]
	texto = [exclui.replace('=', ' ') for exclui in texto]
	texto = [exclui.replace('<', '') for exclui in texto]
	texto = [exclui.replace('>', '') for exclui in texto]
	texto = [exclui.replace(' |', '') for exclui in texto]

	return texto

def var(text):
	val = text[0]
	val = val.split(' ')
	for j in range(len(val)):
		if val[j].isdigit():
			val[j] = int(val[j])

	return val


def checkpoint():
	for i in range(len(undo)):
			if 'n' in undo[i]:
				for j in sta[i]:
					if type(j) is str:
						pos = valores.index(j) 
						valores[pos + 1] = aux[pos + 1]

def tranferencia(vet):
	vet = vet.replace('T', '')
	pos = int(vet[0]) - 1
	vet = vet.split(',')
	for j in range(len(vet)):
		if vet[j].isdigit():
			vet[j] = int(vet[j])
	t = int(vet[0])-1

	return [vet[1], vet[2], vet[3]], t

def redo(pos, sta):
	for x in range(len(sta[pos])):
		if type(sta[pos][x]) is str:
			posicao = valores.index(sta[pos][x])
			valores[posicao + 1] = aux[posicao + 1]


def undof():
	aux.reverse()
	valores.reverse()
	for est in range(len(undo)):
		if 's' in undo[est]:
			for x in range(len(sta[est])):
				if type(sta[est][x]) is str:
					posicao = aux.index(sta[est][x])
					aux[posicao - 1] = sta[est][x+1]
					valores[posicao - 1] = aux[posicao - 1]
			sta[est] = 'Transacao Abortada'
		#if 'ckpt' in undo[est]:
			#print(i)
			#print("foi")
			#break
	aux.reverse()
	valores.reverse()



texto = log()
valores = var(texto)
aux = var(texto)
texto.pop(0)

print ("Valores iniciais:", valores, "\n")
print ("Vetor auxiliar:", aux, "\n")

sta = []
undo = []
for i in texto:
	if 'start' in i:
		sta.append([])
		undo.append('s')
	elif 'commit' in i:
		pos = int(i[-1]) - 1
		redo(pos, sta)
		undo[pos] = 'n'

	elif 'Start CKPT' in i:
		#undo.append('ckpt')
		if 'End CKPT' in texto:
			checkpoint()
	elif 'End CKPT' in i:
		print(".")
	else:
		transfere, ide = tranferencia(i)
		sta[ide].extend(transfere)
		for x in range(len(sta[ide])):
			if type(sta[ide][x]) is str:
				posicao = aux.index(sta[ide][x])
				aux[posicao + 1] = sta[ide][x+2]
print("\n")
for tran in sta:
	print(tran)

print("\n")
print("Vetor auxiliar:", aux, "\n")
print("Transações que farão Undo:", undo, "\n")
undo.reverse()
sta.reverse()

undof()

undo.reverse()
sta.reverse()
for tran in sta:
	print(tran)

print("\n")
print("Vetor auxiliar:", aux, "\n")
print ("Valores salvos:", valores)