turno = input("Em qual turno você estuda? (manhã/tarde/noite): ").lower()

if turno == "manhã":
    print("Bom Dia!")
elif turno == "tarde":
    print("Boa Tarde!")
elif turno == "noite":
    print("Boa Noite!")
else:
    print("Valor Inválido!")