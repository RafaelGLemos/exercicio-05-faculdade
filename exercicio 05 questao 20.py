
"""Informe o dia, mês e ano que nasceu.
Informe o dia, mês e ano atual.
Se (dia e mês) for maior que o dia e mês atual 
então  diminuir 2023 do ano que nasceu - 1, 
se não diminuir 2023 do ano que nasceu apenas. """


dia = int(input("Informe o dia que nasceu: "))
mes = int(input("Informe o mes que nasceu: "))
ano = int(input("Informe o ano que nasceu: "))

dia2 = int(input("Informe o dia que é hoje: "))
mes2 = int(input("Informe o mes que hoje: "))
ano2 = int(input("Informe o ano que hoje: "))

if (dia and mes) < (dia2 and mes2):
    print("Sua idade é: ", (ano2 - ano))

elif (dia < dia2) and (mes == mes2):
    print("Sua idade é: ", (ano2 - ano))

elif (dia == dia2) and (mes == mes2):
    print("Sua idade é: " + str(ano2-ano) +
          " Parabéns, você está aniversáriando hoje!!")

elif mes < mes2:
    print("Sua idade é: ", (ano2 - ano))

else:
    print("Sua idade é: " + str((ano2 - ano) - 1))
