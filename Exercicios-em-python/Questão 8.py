'8. Elaborar um algoritmo que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares disponíveis com o usuário.'

valorDolar=float(input("Informe um valor em dolar: "))
cotacao=float(input("Informe a cotação atual: "))
real=valorDolar*cotacao
print("O valor convertido em R$ ",real)