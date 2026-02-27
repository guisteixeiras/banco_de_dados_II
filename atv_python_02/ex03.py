letra = input("Digite uma letra ").lower()

if len(letra) !=1 or not letra.isalpha():
    print("Digite apenas letras válidas!")
else:
    vogais = "aeiou"
    if letra in vogais:
        print(f"A letra '{letra}' é uma VOGAL.")
    else: 
        print(f"A letra '{letra}' é uma CONSOANTE.")