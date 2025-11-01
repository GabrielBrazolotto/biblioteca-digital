from utils import listar_documentos, adicionar_documento, remover_documento, renomear_documento

def menu():
    while True:
        print("\n--- Biblioteca Digital ---")
        print("1. Listar documentos")
        print("2. Adicionar documento")
        print("3. Remover documento")
        print("4. Renomear documento")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            tipos = listar_documentos()
            for tipo, docs in tipos.items():
                print(f"{tipo}: {docs}")
        elif escolha == '2':
            origem = input("Caminho do arquivo: ")
            adicionar_documento(origem)
        elif escolha == '3':
            nome = input("Nome do documento: ")
            remover_documento(nome)
        elif escolha == '4':
            nome_antigo = input("Nome antigo: ")
            nome_novo = input("Nome novo: ")
            renomear_documento(nome_antigo, nome_novo)
        elif escolha == '5':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
