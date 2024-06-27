sp = "paçoca"

print(
"""
+===================================+
| Bem vindo ao meu jogo!            |
| Adivinhe a palavra secreta!       | 
+===================================+
""")

p = input("Digite uma palavra: ")

while p != sp:
    if p != sp:
        print("Ha ha! Você está preso no meu loop!\n")
        p = input("Digite uma palavra: ")
        break
print("Muito bem! Você está livre agora.!\n")
