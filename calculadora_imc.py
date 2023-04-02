print("Calculada de IMC")
print("Digite o peso:")
peso = float(input())
print("Digite o altura:")
altura = float(input())

imc = peso / (altura * altura)

print("IMC:", round(imc, 2))

if imc <= 18.5 :
    print("🔸 Abaixo do peso")
elif imc > 18.5 and imc <= 24.9:
    print("🔸 Normal")
elif imc >= 25 and imc <= 29.9:
    print("🔸 Sobrepeso / Obesidade grau I")
elif imc >= 30 and imc <= 39.9:
    print("🔸 Obesidade grau II")
else: 
    print("🔸 Obesidade grau III")

