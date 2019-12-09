salario_hora = int(input("Digite o valor do salário por hora R$: "))
print("O salario por hora é igual a: ", salario_hora)

horas_semanais = int(input("Digite as horas semanais de trabalho: "))
dias = int(input("Digite o número de dias de trabalho na semana: "))

horas_mes = horas_semanais * dias
print("O número de horas trabalhadas ao mês é: ", horas_mes)

salario = salario_hora * horas_mes
print("O salário total ao mês é R$: ", salario)
