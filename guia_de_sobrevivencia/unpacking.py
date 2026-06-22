# Unpacking permite extrair os valores de uma estrutura de dados (como listas, tuplas ou dicionários) 
# e os atribua a variáveis individuais de forma concisa e legível. 
# Isso é especialmente útil em uma estrutura de dados complexa e deseja acessar seus elementos de maneira mais direta.

# basic list/tuple unpacking
name, age = ("Mateus", 28)
print(f"{name} is {age} years old")
 
people = (
    {
        "name" : "Mateus",
        "age" : 28
    },
    {
        "name" : "Joao",
        "age" : 29
    },
    {
        "name" : "Teste",
        "age" : 29
    },
    {
        "name" : "Gabriel",
        "age" : 29
    },
)
 
# unpack a tuple of dicts
for person in people:
    name, age = person.values()
    print(f"{name} is {age} years old")
 
# ignore specific field with _
for person in people:
    name, _ = person.values()
    print(f"His name is {name}")
 
# unpack with * (list)
first, *middle, last = people
print(middle)
 
def print_people_info(name, age):
    print(f"{name} is {age} years old")
 
# unpack with ** (dict)
for person in people:
    print_people_info(**person)