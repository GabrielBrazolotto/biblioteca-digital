# Relatório de Testes - Sistema Biblioteca Digital

## 1. Objetivo
Testar todas as funcionalidades do sistema para garantir que os arquivos digitais possam ser adicionados, listados, renomeados e removidos corretamente.

---

## 2. Funcionalidades testadas

### 2.1 Listar documentos
- Função: `listar_documentos()`
- Resultado: Todos os arquivos da pasta `docs/` foram listados corretamente, separados por tipo de arquivo (PDF, MD, etc.).
- Status: ✅ OK

### 2.2 Adicionar documento
- Função: `adicionar_documento()`
- Teste: Adição do arquivo `TEMP.pdf` da pasta `tests/` para `docs/`.
- Resultado: Arquivo adicionado com sucesso. Caso o arquivo já exista na pasta `docs/`, a função evita a cópia duplicada.
- Status: ✅ OK

### 2.3 Renomear documento
- Função: `renomear_documento()`
- Teste: Renomeação do arquivo `TEMP.pdf` para `TEMP_RENOMEADO.pdf`.
- Resultado: Arquivo renomeado corretamente e refletido na listagem.
- Status: ✅ OK

### 2.4 Remover documento
- Função: `remover_documento()`
- Teste: Remoção do arquivo `TEMP_RENOMEADO.pdf`.
- Resultado: Arquivo removido com sucesso. Tentativa de remover arquivo inexistente não gera erro.
- Status: ✅ OK

### 2.5 Menu CLI
- Arquivo: `main.py`
- Teste: Todas as opções interativas (adicionar, listar, renomear, remover) testadas no terminal.
- Resultado: Fluxo completo do menu funcionando corretamente.
- Status: ✅ OK

---

## 3. Observações
- Todos os testes foram realizados com arquivos de exemplo.  
- O sistema está preparado para manipular arquivos de diferentes formatos digitais (PDF, ePUB, MD).  
- Feedback de usuários será registrado para possíveis ajustes.
