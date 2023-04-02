# digitar distância percorrida:
# digitar quantidade total de combustível gasto:
# dividir distância percorrida por combustivel gasto, UNIdade KM/L
# Mostrar na tela o consumo médio

distancia = float(input("informe em KM a distância percorrida: "))
litros = float(input("Informe em Litros a quantidade de combustível gasto: "))

consumoMedio = (distancia / litros)

print("O consumo médio do seu carro é: ", consumoMedio, "KM/L")
