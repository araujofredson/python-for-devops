# List Comprehensions são uma forma de criar listas de forma concisa e legível, utilizando uma única linha de código. 
# Elas permitem aplicar uma expressão a cada elemento de um iterável (como uma lista ou tupla) 
# e opcionalmente filtrar elementos com base em uma condição.

nomes = ("Mateus", "Joao", "Gabriel", "Marcos", "Matheus", "Lucas", "Marcelo")
 
nomes_upper = [ nome.upper() for nome in nomes if nome.startswith("M") ]
print(nomes_upper)