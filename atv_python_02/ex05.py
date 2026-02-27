refri = float(input("Preço do refrigerante: "))
cerveja = float(input("Preço da cerveja: "))
agua = float(input("Preço da água: "))

if refri < cerveja and refri < agua:
    print("Compre o refrigerante.")
elif cerveja < agua:
    print("Compre a cerveja.")
else:
    print("Compre a água.")