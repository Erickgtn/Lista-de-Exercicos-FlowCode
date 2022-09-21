'Esturuta de Repetição'
'21. Escrever um algoritmo que leia os dados de “N” pessoas (nome, sexo, idade e saúde) e informe se está apta ou não para cumprir o serviço militar obrigatório. Informe os totais.'


totalAptos = 0
totalNaoAptos = 0

n=int(input("Informe quantidade de pessoas: "))
for i in range(n):
  nome=input("Nome: ")
  sexo=input("Sexo (M/F): ")
  idade=int(input("Idade: "))
  saude=input("Saude (Saudável Sim/Nao): ")
  if(idade>=18 and sexo==("M" or "m") and saude=="Sim"):
    print("Apto para servir\n")
    totalAptos+=1
  else:
    print("Não apto para servir\n")
    totalNaoAptos+=1
print("Total de Aptos a servir: ",totalAptos)
print("Total de não aptos a servir: ",totalNaoAptos)