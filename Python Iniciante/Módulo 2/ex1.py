""" EXercicio 1
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa num dicionário e
todos os dicionários numa lista. No final, mostre:
* Quantas pessoas foram cadastradas;
* A média de idade;
* Uma lista com as mulheres;
* Uma lista de pessoas com idade acima da média;
"""
list_people = []

name = input("Nome: ")
sex = input("Sexo: ").upper()
age = int(input("Idade: "))

first_person = {"nome": name, "sexo": sex, "idade": age}
list_people.append(first_person)

while True:
    x = input("Adicionar outra pessoa? S/N").upper()
    if x == "S":
        name = input("Nome: ")
        sex = input("Sexo: ").upper()
        age = int(input("Idade: "))
        dict_person = {"nome": name, "sexo": sex, "idade": age}
        list_people.append(dict_person)
    else:
        print("Encerrando programa.")
        break

print(list_people)
print(f'{len(list_people)} pessoas foram cadastradas.')

soma_idade = 0

for c in range(0, len(list_people)):
    for key in list_people:
        soma_idade += list_people[c]['idade']
        print(c)

print(soma_idade)


