'Decisão'
'25. Faça um algoritmo que leia dois números e identifique se são iguais ou diferentes. Caso eles sejam iguais imprima uma mensagem dizendo que eles são iguais. Caso sejam diferentes, informe qual número é o maior, e uma mensagem que são diferentes'

numero1 = int(input("Informe um número: "))
numero2 = int(input("Informe um outro número: "))

if (numero1 == numero2):
  print("Numeros iguais!")
elif (numero1 != numero2):
    print("Numeros diferentes!")
    if(numero1 > numero2):
      print(numero1," É maior que ",numero2)
    else:
      print(numero2," É maior que ",numero1)
