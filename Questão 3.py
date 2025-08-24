# Programa 3: Cálculo do Imposto de Renda

salario = float(input("Digite o valor do salário: R$ "))

if salario <= 2259.20:
    imposto = 0
elif salario <= 2826.65:
    imposto = salario * 0.075
elif salario <= 3751.05:
    imposto = salario * 0.15
elif salario <= 4664.68:
    imposto = salario * 0.225
else:
    imposto = salario * 0.275

print(f"Imposto de Renda a pagar: R$ {imposto:.2f}")
