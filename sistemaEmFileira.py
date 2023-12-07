import queue

def desinfileirar(q, num):
    if num > 0:
        q.put(num)
    else:
        print("Positivo:")
def dobro(q):
    if not q.empty():
        num = q.get()
        print(f"Dobro: {num * 2}")
    else:
        print("Vazia.")
def imprimir(q):
    while not q.empty():
        num = q.get()
        print(f"Desenfileirado: {num}")

def main():
    q = queue.Queue()

    while True:
        print("1.Positivo")
        print("2.Dobro")
        print("3.Valores")
        print("4.Encerrar")
        choice = input("Escolha:")

        if choice == "1":
            num = int(input("Qual o numero positivo:"))
            desinfileirar(q, num)
        elif choice == "2":
            dobro(q)
        elif choice == "3":
            imprimir(q)
        elif choice == "4":
            break
        else:
            print("Invalido")

if __name__ == "__main__":
    main()