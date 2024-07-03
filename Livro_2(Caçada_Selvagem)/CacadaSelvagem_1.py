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

print("Qual a senha?")
senha = str(input().upper())
print("Digite cada linha da mensagem secreta.")
print("Quando terminar, digite FIM.")
print()

mensagem_cripto = ""
mensagem_final = ""
j = 0

while mensagem_cripto != "FIM":
	
	mensagem_cripto = str(input().upper())
	if mensagem_cripto == "FIM":
		print("Execucao terminada!")
		break
	mensagem_final = ""
	for i in range(0,len(mensagem_cripto)):
		letra_cripto = mensagem_cripto[i]
		if (letra_cripto < 'A' or letra_cripto > 'Z'):
			mensagem_final = mensagem_final + letra_cripto
		else:
			if j > len(senha) - 1:
				j = 0
			ascii_senha = ord(senha[j]) - ord('A') + 1
			ascii_cripto = ord(letra_cripto) - ord('A') + 1
			if ascii_senha <= ascii_cripto:
				ascii_senha = ascii_senha + 26
			ascii_letra_final = ascii_senha - ascii_cripto
			mensagem_final = mensagem_final + chr(ascii_letra_final + ord('A') - 1)
			j = j + 1
	print(mensagem_final)
	print()