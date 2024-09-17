nome_maisvelho = " "
somatotal = 0
maisvelho = 0
mulheres = 0
for p in range(1, 5):
    print("----", p, "' PESSOA -----")
    nome = str(input("nome: "))
    idade = int(input("idade: "))
    somatotal += idade
    sexo = str(input("Sexo [M ou H]: ")).strip().upper()
    if sexo == "H":
        if idade > maisvelho:
            maisvelho = idade
            nome_maisvelho = nome
    elif sexo == "M":
        if idade < 20:
           mulheres += 1

media = somatotal / 4

print("A média da idade total de pessoas é de ", media, " anos.")
print("O homem mais velho tem {} anos e se chama {}.".format(maisvelho, nome_maisvelho))
print("Ao todo são {} mulheres que são menores que 20 anos.".format(mulheres))
