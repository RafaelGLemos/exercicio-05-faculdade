# receber 2 numeros A e B
# inverter os numeros, na qual A passa a ser B e B passa a ser A.
# informar na tela.

a = int(input("Informe um número para A: "))
b = int(input("Informe um número para B: "))

c = a

a = b

b = c

print(" O número de A agora é: " + str(a) +
      " e o número de B agora é: " + str(b))
