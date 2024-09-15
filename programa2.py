def contar_letra_a(s):
    return s.lower().count('a')

entrada = input("Digite uma string: ")
quantidade = contar_letra_a(entrada)
if quantidade > 0:
    print(f"A letra 'a' (maiúscula ou minúscula) aparece {quantidade} vez(es) na string.")
else:
    print("A letra 'a' (maiúscula ou minúscula) não aparece na string.")
