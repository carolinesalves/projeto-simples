h = float(input("Digite sua altura: "))
print(h)

s = input("Digite o sexo: ")
print(s)

peso = 0
if s == "masculino":
    peso = (72.7 * h) - 58
    print("O peso ideal para altura de {} m é {} kg ".format(h, round(peso,1)))
elif s == "feminino":
    peso = (62.1 * h) - 44.7
    print("O peso ideal para altura de {} m é {} kg ".format(h, round(peso,1)))
else:
    print("Entrada Invalida")

