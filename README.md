


# 💸 Organizador de Despesas – Python

Um projeto simples e funcional para **gerenciamento de despesas pessoais**, desenvolvido em Python.  
Permite registrar gastos, listar, atualizar, remover, gerar resumos e exportar tudo para Excel.

Este sistema é ideal para quem quer aprender lógica, CRUD, manipulação de arquivos JSON e criação de planilhas com `openpyxl`.

---

## 📌 Funcionalidades

### 🔹 CRUD Completo
- **Adicionar** despesas  
- **Listar** todas as despesas  
- **Atualizar** uma despesa existente  
- **Remover** despesas por ID  

### 🔹 Resumos
- **Resumo total**: soma geral de todos os gastos  
- **Resumo por mês**: filtra despesas pelo mês atual  

### 🔹 Exportação
- **Exportar para Excel (.xlsx)** com todas as despesas cadastradas

### 🔹 Sistema de Armazenamento
- Despesas salvas em arquivo **JSON** (`despesas.json`)  
- Garante persistência mesmo após fechar o programa  

---

## 🗂 Estrutura do Projeto

```

Controle de despesas.py     # Código principal do sistema
despesas.json               # Arquivo de armazenamento (criado automaticamente)
despesas.xlsx               # Exportação em Excel (opcional)

````

---

## 🛠 Tecnologias Utilizadas

- **Python 3**
- `json` – armazenamento local
- `openpyxl` – geração de planilhas Excel
- `os` e `datetime` – utilidades do sistema

---

## 🚀 Como executar o projeto

### 1️⃣ Instale as dependências
```bash
pip install openpyxl
````

### 2️⃣ Execute o programa

```bash
python "Controle de despesas.py"
```

Após isso, o menu principal será exibido:

```
===== ORGANIZADOR DE DESPESAS =====
1 - Adicionar despesa
2 - Listar despesas
3 - Atualizar despesa
4 - Remover despesa
5 - Resumo total
6 - Resumo por mês
7 - Exportar para Excel
8 - Limpar todas as despesas
0 - Sair
```

---

## 📊 Exportação para Excel

Ao selecionar a opção **7**, o sistema gera automaticamente o arquivo:

```
despesas.xlsx
```

Com as colunas:

* ID
* Descrição
* Valor
* Categoria
* Data

---

## 🐞 Possíveis Problemas

### ❗ O arquivo `despesas.json` não existe

Ele será criado automaticamente na primeira execução.

### ❗ Erro ao atualizar despesas

Verifique se o ID digitado realmente existe na lista de despesas.

---

## 📈 Melhorias futuras (sugestões)

* Interface gráfica com **Tkinter** ou **PySide6**
* Gráficos de gastos mensais
* Validação automática de datas
* Autenticação do usuário
* Suporte a múltiplos perfis de despesas
* Exportação em PDF

---

## 📄 Licença

Este projeto é livre para uso **pessoal e educacional**.

---

## ✨ Autor

**Mateus Teixeira**
Projeto desenvolvido para estudo e aprimoramento em Python.

