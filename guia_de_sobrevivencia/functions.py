def calcular_media(nota1, nota2):
    # Soma as notas e divide por 2
    media = (nota1 + nota2) / 2
    return media

# Chamando a função
resultado = calcular_media(7.5, 9.0)
print(f"A média do aluno é: {resultado}")



# 1. lista com os nomes
nomes = ["ana", "maria", "pedro", "luis"]

# 2. Cria a função que gera os e-mails
def criar_emails(lista_de_nomes):
    for nome in lista_de_nomes:
        email = nome + "@foobar.com"
        print(email)

# 3. Chamamos a função passando a nossa lista
criar_emails(nomes)
