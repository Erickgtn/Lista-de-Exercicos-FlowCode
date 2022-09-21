'Esturuta de Repetição'
'20. A concessionária de veículos “CARANGO VELHO” está vendendo os seus veículos com desconto. Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente de vários carros. O desconto deverá ser calculado de acordo com o ano do veículo. Até 2000 - 12% e acima de 2000 - 7%. O sistema deverá perguntar se deseja continuar calculando desconto até que a resposta seja: “(N) Não” . Informar total de carros com ano até 2000 e total geral.'

totalCarroAntigo =0
totalCarro = 0

resp = 's'

while (not resp in ['N','n']):
    valor = float(input("Informe o valor do veiculo: "))
    ano = int(input("Informe o ano do veiculo: "))
    if ano<=2000:
      totalCarroAntigo=+1
      valorFinal = valor - valor*0.12
      print("O valor com desconto é de:",valorFinal)
      
    elif ano > 2000:
      totalCarro = totalCarro + 1
      valorFinal = valor - valor*0.07
      print("O valor com desconto é de:",valorFinal)
    resp = input("Deseja continuar calculando? S-sim ou N-Não\n")

print("Total de carros até  ano 2000: ",totalCarro)
print("Total de carros: ",int(totalCarroAntigo + totalCarro))
