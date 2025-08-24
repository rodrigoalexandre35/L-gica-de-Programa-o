# Programa 5: Validação de senha

senha = input("Digite uma senha: ")

if len(senha) < 8:
    print("Senha inválida: deve ter pelo menos 8 caracteres.")
elif not any(c.isupper() for c in senha):
    print("Senha inválida: deve conter pelo menos uma letra maiúscula.")
elif not any(c.isdigit() for c in senha):
    print("Senha inválida: deve conter pelo menos um número.")
elif " " in senha:
    print("Senha inválida: não pode conter espaços em branco.")
else:
    print("Senha válida!")
