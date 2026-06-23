names = ["Mateus", "João", "Maria", "Ana"]

for name in names:
    if name == "Mateus":
        print(f"A lista contém Mateus")

# a biblioteca "in" permite verificar se um elemento está presente em uma lista de forma mais concisa e legível e substitui a necessidade de um loop for para percorrer a lista e verificar cada elemento individualmente.
if "João" in names:
    print(f"A lista contém João")