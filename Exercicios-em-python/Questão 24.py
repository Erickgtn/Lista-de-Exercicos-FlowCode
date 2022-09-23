'Decisão'
'24. Faça um algoritmo que receba “N” números e mostre positivo, negativo ou zero para cada número.'

n = int(input("Informe quantos numeros processar: "))

for i in range(n):
  numero=int(input("Informe um número: "))
  if (numero > 0 ):
    print("Numero Positivo!")
  elif (numero < 0):
    print("Numero Negativo!")
  elif(numero == 0):
    print("Número igual 0!")