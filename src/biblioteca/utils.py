import os
import shutil

def listar_documentos(caminho='docs'):
    arquivos = os.listdir(caminho)
    tipos = {}
    for arquivo in arquivos:
        ext = arquivo.split('.')[-1].lower()
        tipos.setdefault(ext, []).append(arquivo)
    return tipos

def adicionar_documento(origem, destino='docs'):
    shutil.copy(origem, destino)
    print(f"Documento {origem} adicionado à biblioteca.")

def remover_documento(nome, caminho='docs'):
    arquivo = os.path.join(caminho, nome)
    if os.path.exists(arquivo):
        os.remove(arquivo)
        print(f"Documento {nome} removido.")
    else:
        print(f"Documento {nome} não encontrado.")

def renomear_documento(nome_antigo, nome_novo, caminho='docs'):
    arquivo_antigo = os.path.join(caminho, nome_antigo)
    arquivo_novo = os.path.join(caminho, nome_novo)
    if os.path.exists(arquivo_antigo):
        os.rename(arquivo_antigo, arquivo_novo)
        print(f"Documento renomeado para {nome_novo}.")
    else:
        print(f"Documento {nome_antigo} não encontrado.")
