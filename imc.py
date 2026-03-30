Peso = float(input("Digite o seu peso:"))
Altura = float(input("Digite sua altura:").replace(",","."))
imc = Peso / Altura ** 2

print("Seu IMC é:", round(imc, 2))
