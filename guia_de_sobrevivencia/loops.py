# loops são estruturas de controle que permitem executar um bloco de código repetidamente enquanto uma condição for verdadeira.


nomes = ("Mateus", "Joao", "Gabriel")
 
for nome in nomes:
    print(nome)
 
print("")
 
for item in range(len(nomes)):
    print(f"{item} - {nomes[item]}")
 
print("")
 
count = 0
while count < len(nomes):
    print(nomes[count])
    count+=1