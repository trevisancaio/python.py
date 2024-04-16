def calcular_imc(peso, altura):
    return peso / (altura ** 2)

while True:
    try:
        altura = float(input("Digite sua altura em metros: "))

        if altura <= 0:
            continue

        peso = float(input("Digite seu peso em quilogramas: "))

        if peso <= 0:
            continue

        imc = calcular_imc(peso, altura)
        imc_arredondado = round(imc, 2)
        print(f"Seu IMC é: {imc_arredondado}")

        if imc_arredondado <= 18.4:
            print("Você está abaixo do peso.")
        elif imc_arredondado <= 24.9:
            print("Seu peso está normal.")
        elif imc_arredondado <= 29.9:
            print("Você está acima do peso.")
        elif imc_arredondado <= 34.9:
            print("Você está com obesidade grau I.")
        
    except ValueError:
        print("Por favor, insira apenas números.")
