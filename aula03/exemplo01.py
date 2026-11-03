salario_atual = float(input("Informe o valor do salário: R$ "))
aumento_percentual = float(input("Informe o percentual de aumento: "))

valor_aumento = salario_atual * (aumento_percentual / 100)
valor_final = salario_atual + valor_aumento

print(f"Salário inicial: R$ {salario_atual:.2f}")
print(f"Percentual de aumento: {aumento_percentual:.2f} %")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Salário final: R$ {valor_final:.2f}")

# teste de versionamento no GitHub
print()
valor_br = f"{valor_final:_.2f}".replace(".", ",").replace("_", ".")
print(f"Salário final (padrão BR): R$ {valor_br}")