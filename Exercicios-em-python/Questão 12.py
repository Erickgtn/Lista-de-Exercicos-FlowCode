'12. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados, primeiro os impostos sobre o custo de fábrica, e depois a percentagem do distribuidor sobre o resultado). Supondo que a percentagem do distribuidor seja de 28% e os impostos 45%. Escrever um algoritmo que leia o custo de fábrica de um carro e informe o custo ao consumidor do mesmo.'

custoDeFabrica = float(input("Informe o custo de fabrica: "))
impostos = custoDeFabrica * 0.45
distribuidor = (custoDeFabrica + impostos ) *0.28

print(" O Valor final sera de R$ ",custoDeFabrica+impostos+distribuidor)