nome = input("informe seu nome: ")
salario = float(input("informe seu salário: "))
vendas = float(input("informe o valor total que vendeu no mês: "))

comissao = vendas * 0.15

print("Olá, " + str(nome) + " seu salário no valor de: " + str(salario) +
      " mais sua comissão no valor de " + str(comissao) +
      " dará um total no mês de: " + str(comissao + salario))
