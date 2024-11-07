def calcular_imc(peso, altura):
  """Calcula o IMC com base no peso e altura fornecidos."""
  imc = peso / (altura ** 2)
  return imc

for i in range(3):
  peso = float(input(f"Digite o peso da pessoa {i+1} (em kg): "))
  altura = float(input(f"Digite a altura da pessoa {i+1} (em metros): "))

  imc = calcular_imc(peso, altura)
  print(f"O IMC da pessoa {i+1} é: {imc:.2f}")
  