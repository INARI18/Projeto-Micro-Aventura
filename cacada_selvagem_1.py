#Correcao da mensagem original:

"""
AFVFYFNE KO NQPVSZ MIQOFQN
LVGOFFZ WFJDW AJMIUOZ
EMFVFZSE WKHSHUSW MRUUUKVVZ
GDXYJWGHHKE
JC GUVYE BOCQVZ 48 LZXZG
DAQZBGHD-VO LAN YBJFUK
VM 5 VFFTVLG
"""

#senha: TOPAZIO

print("Qual a SENHA?")
SENHA = str(input().upper())
print("Digite cada linha da mensagem secreta.")
print("Quando terminar, digite FIM.")
print()

MENSAGEM_CRIPTO = ""
MENSAGEM_FINAL = ""
j = 0

while MENSAGEM_CRIPTO != "FIM":
	
	MENSAGEM_CRIPTO = str(input().upper())
	if MENSAGEM_CRIPTO == "FIM":
		print("Execucao terminada!")
		break
	MENSAGEM_FINAL = ""
	for i in range(0,len(MENSAGEM_CRIPTO)):
		LETRA_CRIPTO = MENSAGEM_CRIPTO[i]
		if (LETRA_CRIPTO < 'A' or LETRA_CRIPTO > 'Z'):
			MENSAGEM_FINAL = MENSAGEM_FINAL + LETRA_CRIPTO
		else:
			if j > len(SENHA) - 1:
				j = 0
			ASCII_SENHA = ord(SENHA[j]) - ord('A') + 1
			ASCII_CRIPTO = ord(LETRA_CRIPTO) - ord('A') + 1
			if ASCII_SENHA <= ASCII_CRIPTO:
				ASCII_SENHA = ASCII_SENHA + 26
			ASCII_LETRA_FINAL = ASCII_SENHA - ASCII_CRIPTO
			MENSAGEM_FINAL = MENSAGEM_FINAL + chr(ASCII_LETRA_FINAL + ord('A') - 1)
			j = j + 1
	print(MENSAGEM_FINAL)
	print()