'Esturuta de Repetição'
'19.Escrever um algoritmo que leia o nome e o sexo de 56 pessoas e informe o nome e se ela é homem ou mulher. No final informe total de homens e de mulheres.'


for i in range(5):
  nome = input("Informe seu nome: ")
  sexo = input("Informe seu sexo M/F: ")
  
  if sexo=='m' or sexo=='M':
    print(nome," é homem")
  elif sexo=='f' or sexo=='F':
     print(nome," é mulher")
