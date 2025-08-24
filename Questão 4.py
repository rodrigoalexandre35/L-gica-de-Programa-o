# Programa 4: Verificar divisibilidade

num = int(input("Digite um número entre 1 e 100: "))

if num % 3 == 0 and num % 5 == 0:
    print("Número divisível por 3 e por 5.")
elif num % 3 == 0:
    print("Número divisível por 3")
elif num % 5 == 0:
    print("Número divisível por 5")
else:
    print("Número comum")
