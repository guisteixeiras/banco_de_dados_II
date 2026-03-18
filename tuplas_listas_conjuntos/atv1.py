estoque_despensa = ["Arroz", "Feijão", "Macarrão", "Açúcar", "Café", "Leite"]

estoque_tratado = [item.strip().lower() for item in estoque_despensa]

while True:
    item = input("Digite o item desejado (ou [0] para encerrar): ").strip().lower()

    if item == "0":
        print("Programa encerrado.")
        break

    if item in estoque_tratado:
        print("Item disponível no estoque.")
    else:
        print("Item não disponível no estoque.")