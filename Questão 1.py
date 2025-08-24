# Programa 1: Dia útil ou fim de semana

dia = input("Digite um dia da semana: ").strip().lower()

if dia in ["segunda", "terça", "terca", "quarta", "quinta", "sexta"]:
    print("Dia útil")
elif dia in ["sábado", "sabado", "domingo"]:
    print("Fim de semana")
else:
    print("Dia inválido")
