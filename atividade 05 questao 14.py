"""Informe a temperatura em ºC
fazer conversão em F
exibir na tela o resultado em F"""

temp = int(input("Informe a temperatura em ºC para fazer a conversão em F: "))

tempCalc = ((9 * temp) + 160) / 5

print("A temperatura em Fahrenheit é: " + str(tempCalc) + "F")
