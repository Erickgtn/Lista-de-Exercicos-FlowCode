'Estrutura de decisão'
'Escrever um algoritmo que leia o nome e as três notas obtidas por um aluno durante o semestre. Calcular a sua média (aritmética), informar o nome e sua menção aprovado (media >= 7), Reprovado (media <= 5) e Recuperação (media entre 5.1 a 6.9).'

n1 = float(input("Informe primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
n3 = float(input("Informe terçeira nota: "))

media = (n1+n2+n3)/3

if media >=7:
  print("Aprovado")
elif media >=5 and media <=6:
    print("Recuperação")
else:
  print("Reprovado")