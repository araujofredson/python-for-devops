# listas listas são mutáveis, ou seja, podem ser alteradas depois de criadas
name_list = ["Matheus", "João", "Maria"]
name_list.append("Ana")  # adiciona um elemento no final da lista
print(name_list)

# tuplas tuplas são imutáveis, ou seja, não podem ser alteradas depois de criadas
name_tuple = ("Matheus", "João", "Maria")
print(name_tuple)

# sets sets são mutáveis, mas não permitem elementos duplicados (não mantêm a ordem dos elementos)
name_set = set(name_list)  # converte a lista em um set
name_set.add("novato")
print(name_set)