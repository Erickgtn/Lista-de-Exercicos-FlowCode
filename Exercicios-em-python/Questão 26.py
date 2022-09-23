'Decisão'
'26. Faça um algoritmo que leia um número de 1 a 5 e escreva por extenso. Caso o usuário digite um número que não esteja neste intervalo, exibir mensagem: número inválido'

numero = int(input("Informe um número: "))

if numero == 1:
  print("Um")
elif numero == 2:
  print("Dois")
elif numero == 3:
  print("Tres")
elif numero == 4:
  print("Quatro")
elif numero == 5:
  print("cinco")
else:
  print("Fora do intervalo")