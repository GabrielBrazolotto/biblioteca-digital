# Guia do Usuário - Sistema Biblioteca Digital

## 1. Introdução
O sistema Biblioteca Digital foi desenvolvido para auxiliar bibliotecários na gestão de arquivos digitais (PDF, ePUB, MD, etc.). Ele permite listar, adicionar, renomear e remover documentos de forma rápida e organizada.

---

## 2. Requisitos
- Python 3.12+ instalado
- Estrutura do projeto:
Biblioteca Digital/
├─ src/
│ └─ biblioteca/
├─ docs/
├─ tests/
├─ CONTRIBUTING.md
├─ Test_report.md
└─ User_Guide.md

---

## 3. Como usar

### 3.1 Rodar o sistema
1. Abra o terminal na pasta do projeto:
<!-- bash
cd "D:/IA/Programação python/Biblioteca Digital" -->
### 3.2 Menu principal

O menu possui as seguintes opções:

Listar documentos
Mostra todos os arquivos da pasta docs/ separados por tipo de arquivo.

Adicionar documento
Adiciona um arquivo à biblioteca digital:

Informe o caminho completo ou relativo do arquivo a ser adicionado.

Renomear documento
Permite alterar o nome de um arquivo existente na pasta docs/.

Remover documento
Remove um arquivo existente da pasta docs/.

Sair
Encerra o programa.

### 4. Observações importantes

Evite arquivos duplicados com o mesmo nome na pasta docs/.

Sempre verifique o nome correto ao remover ou renomear documentos.

Para testes ou feedback, utilize arquivos temporários fora da pasta docs/.