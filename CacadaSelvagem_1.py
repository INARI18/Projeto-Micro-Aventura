# Cifra de Vigenère

"""
AFVFYFNE KO NQPVSZ MIQOFQN
LVGOFFZ WF JDW-AJMIVOZ
EMFVFZSE WKH SHUSW MRUUUKVVZ
GDXYJWGHHKE
JC GUVYE BOCQVZ 48 LZXZG
DAQ ZBGHD-VO LAN YBJFUK
VM 5 VFFTVLG
"""

LETRA_FINAL = "" 
j = 0 #indice que percorre a SENHA TOPAZIO

print("Qual a SENHA?")
SENHA = "Topazio" #str(input()) #recebe a SENHA
print("Digite cada linha da LETRA_FINAL secreta.")
print("Quando terminar, digite FIM.")
print() 

MENSAGEM_CRIPTO = "INICIO"

while(MENSAGEM_CRIPTO not in "FIM" or MENSAGEM_CRIPTO not in "fim"):
	MENSAGEM_CRIPTO = str(input())
	if MENSAGEM_CRIPTO == "FIM" or MENSAGEM_CRIPTO == "fim":
		print("Execucao terminada!")
		exit()
	for i in range(0,len(MENSAGEM_CRIPTO)):
		LETRA_CODIGO = MENSAGEM_CRIPTO[i]
		if (LETRA_CODIGO < 'A' or LETRA_CODIGO > 'Z'):
			LETRA_FINAL = LETRA_FINAL + LETRA_CODIGO
		j = j + 1 #avança para o proximo indice da SENHA
		if j > len(SENHA) - 1: #reinicia o indice da SENHA
			j = 0
		ASCII_SENHA = ord(SENHA[j]) - ord('A')+1
		ASCII_CODIGO = ord(LETRA_CODIGO) - ord('A') + 1
		#print(ASCII_SENHA,ASCII_CODIGO)
		if ASCII_SENHA <= ASCII_CODIGO:
			ASCII_SENHA = ASCII_SENHA + 26
		ASCII_LETRA_FINAL = ASCII_SENHA - ASCII_CODIGO
		LETRA_FINAL = LETRA_FINAL + chr(ASCII_LETRA_FINAL + ord('A') - 1)
	print(LETRA_FINAL)
