'Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final do mês.'

nome = input("Informe o nome do vendedor\n")
salario = float(input("Informe o seu salarios\n"))
totalVendas = int(input("Informe o total de vendas efetuadas\n"))
comissao = 0.15*totalVendas
print("Nome: ", nome)
print("Salario Fixo: ",salario)
print("Salario mais comissao: ",salario+comissao)