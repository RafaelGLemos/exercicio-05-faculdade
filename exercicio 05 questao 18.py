"""Informe a cotação do dolar turismo hoje. adquirir cotação no google.com
Informe quantos reais deseja levar para viagem. 
dividir a quantidade de reais que possui para a viagem pelo valor do dolar turismo.
exibir na tela a quantidade de dolar que vai levar para viagem."""

dolar = float(input("Informe o valor do Dólar turismo hoje. Adquirir no google.com: "))
reais = float(input("Informe quantos reais deseja levar para a viagem"))

conversao = reais / dolar

print("Você levará para viagem um total de " + str(conversao) + " dólares. boa viagem!")
