altura = float(input("Digite sua altura (em metros): "))
peso = float(input("Digite seu peso (em quilogramas): "))

imc = peso / (altura ** 2)

if imc < 17:
    print("Muito abaixo do peso - IMC: %.1f" % imc)
elif 17 <= imc < 18.5:
    print("Abaixo do peso - IMC: %.1f" % imc)
elif 18.5 <= imc < 25:
    print("Peso normal - IMC: %.1f" % imc)
elif 25 <= imc < 30:
    print("Acima do peso - IMC: %.1f" % imc)
elif 30 <= imc < 35:
    print("Obesidade I - IMC: %.1f" % imc)
elif 35 <= imc < 40:
    print("Obesidade II (severa) - IMC: %.1f" % imc)
else:
    print("Obesidade III (mórbida) - IMC: %.1f" % imc)

assert isinstance(altura, float) and isinstance(peso, float), "Entrada inválida"
