valor_salario = float(input("Informe o valor do salário: R$ "))
aumento_percentual = float(input("Informe o percentual de aumento: "))

valor_final = valor_salario + (valor_salario * aumento_percentual / 100)

print(f"Salário inicial: R$ {valor_salario:.2f}")
print(f"Percentual de aumento: {aumento_percentual:.2f}%")
print(f"Valor do aumento: R$ {valor_final - valor_salario:.2f}")
print(f"Salário final: R$ {valor_final:.2f}")

print('*** TESTE 1 ***')
valor_br = f"{valor_final:_.2f}"
valor_br = valor_br.replace(".", ",").replace("_", ".")
print(f"valor_br: R$ {valor_br}")

print('*** TESTE 2 ***')
valor_br = f"{valor_final:_.2f}".replace(".", ",").replace("_", ".")
print(f"valor_br: R$ {valor_br}")