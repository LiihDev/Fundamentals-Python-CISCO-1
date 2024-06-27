import random

sn = random.randint(1,20)

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhe o número que tenho    |
| escolhido para você.             | |
+===================================+
""", {sn})

n = int(input("Digite um número: "))

while n != sn:
    if n != sn:
        print("Ha ha! Você está preso no meu loop!\n")
        n = int(input("Digite um número: "))
print("Muito bem, trouxa! Você está livre agora.!\n")
