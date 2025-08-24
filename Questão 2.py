# Programa 2: Identificação de criatura

horario = input("Informe o horário (dia/noite): ").strip().lower()
caracteristica1 = input("Informe a primeira característica: ").strip().lower()
caracteristica2 = input("Informe a segunda característica: ").strip().lower()

if horario == "noite" and caracteristica1 == "garras" and caracteristica2 == "evita prata":
    print("Lobisomem")
elif (horario in ["dia", "noite"]) and caracteristica1 == "rápido" and caracteristica2 == "ataca em grupo":
    print("Nekker")
elif caracteristica1 == "não tem olhos" and caracteristica2 == "imita vozes humanas":
    print("Mímico")
else:
    print("Criatura desconhecida. Prepare-se para o pior.")
