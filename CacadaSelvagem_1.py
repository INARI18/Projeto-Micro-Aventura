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

letraFinal = "" 
j = 0 #indice que percorre a senha TOPAZIO

print("Qual a senha?")
senha = "Topazio" #str(input()) #recebe a senha
print("Digite cada linha da letraFinal secreta.")
print("Quando terminar, digite FIM.")
print() 

mensagemCripto = "INICIO"

while(mensagemCripto != "FIM" and mensagemCripto != "fim"):
	mensagemCripto = str(input())
	if mensagemCripto == "FIM" or mensagemCripto == "fim":
		print("Execucao terminada!")
		exit()
	for i in range(0,len(mensagemCripto)):
		letra_Codigo = mensagemCripto[i]
		if (letra_Codigo < 'A' or letra_Codigo > 'Z'):
			letraFinal = letraFinal + letra_Codigo
		j = j + 1 #avança para o proximo indice da senha
		if j > len(senha) -1: #reinicia o indice da senha
			j = 0
		ascii_Senha = ord(senha[j]) - ord('A')+1
		ascii_Codigo = ord(letra_Codigo) - ord('A')+1
		#print(ascii_Senha,ascii_Codigo)
		if ascii_Senha <= ascii_Codigo:
			ascii_Senha = ascii_Senha + 26
		ascii_letraFinal = ascii_Senha - ascii_Codigo
		letraFinal = letraFinal + chr(ascii_letraFinal + ord('A') -1)
	print(letraFinal)