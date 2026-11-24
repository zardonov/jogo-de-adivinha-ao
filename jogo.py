import random

numero_secreto = random.randint(1, 100)
tentativas = 0

print("Jogo de Adivinhação")
print("Pensei em um número de 1 a 100. Tente descobrir!")

while True:
    try:
        palpite = int(input("Digite seu palpite: "))
    except ValueError:
        print("Digite apenas números.")
        continue

    tentativas += 1

    if palpite < numero_secreto:
        print("O número secreto é maior. Tente de novo!")
    elif palpite > numero_secreto:
        print("O número secreto é menor. Tente de novo!")
    else:
        print("Parabéns! Você acertou!")
        print("Número de tentativas:", tentativas)
        break
