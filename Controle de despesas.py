import json
import os
from openpyxl import Workbook
from datetime import datetime

ARQUIVO = 'despesas.json'

#----------------------- Funções de Arquivo -----------------------#

def carregar_despesas():
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            print('Erro ao carregar despesas. O arquivo pode estar corrompido.')
            return []
    else:
        return []

def salvar_despesas(despesas):
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(despesas, f, indent=4, ensure_ascii=False)
    print('Despesas salvas com sucesso!')

#----------------------- Funções internas -----------------------#   

def gerar_id(despesas):

    if not despesas:
        return 1
    return max(d['id'] for d in despesas) + 1

#----------------------- Crud: criar -----------------------#

def adicionar_despesas():
    despesas = carregar_despesas()

    descricao = input('Descrição da despesa: ')
    
    while True:
        try:
            valor = float(input('Valor:'))
            break
        except ValueError:
            print('Valor inválido. Digite um número válido.')

    categoria = input('Categoria (ex: comida, transporte, lazer): ')
    data = input('Data (AAAA-MM-DD) ou Enter para hoje: ') or datetime.now().strftime('%Y-%m-%d')

    nova_despesa = {
        'id': gerar_id(despesas),
        'descricao': descricao,
        'valor': valor,
        'categoria': categoria,
        'data': data
    }

    despesas.append(nova_despesa)
    salvar_despesas(despesas)
    print('\n Despesa adicionada com sucesso!\n')


# ------------------- CRUD: Listar --------------------#

def listar_despesas():
    despesas = carregar_despesas()
    if not despesas:
        print('Nenhuma despesa cadastrada ainda!')
        return

    print("\n===== LISTA DE DESPESAS =====")
    for d in despesas:
         print(f"ID: {d['id']} | {d['data']} | {d['descricao']} - R$ {d['valor']} ({d['categoria']})")
    print("")


# ------------------- CRUD: Atualizar --------------------#


    def atualizar_despesa():
        despesas = carregar_despesas
        listar_despesas()

        try:
            id_alvo = int(input('Digite a id q deseja atualizar: '))
        except ValueError:
            print('ID invalido')
            return
        
        for d in despesas:
            if d['id'] == id_alvo:
                print('\n--- Deixe em branco para manter o valor atual ---"')

            nova_desc = input(f"Nova descrição ({d['descricao']}): ") or d['descricao']
            novo_valor = input(f"Novo valor ({d['valor']}): ")
            nova_cat = input(f"Nova categoria ({d['categoria']}): ") or d['categoria']
            nova_data = input(f"Nova data ({d['data']}): ") or d['data']    

            d['descricao'] = nova_desc
            d['categoria'] = nova_cat
            d['data'] = nova_data

            if novo_valor:
                try:
                    d['valor'] = float(novo_valor)
                except:
                    print('Valor inválido! Mantendo o valor antigo.')

            salvar_despesas(despesas)
            print("\n✔ Despesa atualizada!\n")
            return

    print("\n ID não encontrado!\n")


  # ------------------- CRUD: Remover --------------------#

def remover_despesa():
    despesas = carregar_despesas()
    listar_despesas()

    try:
        id_alvo = int(input('Digite o ID da despesa que deseja remover:'))
    except ValueError:
        print("ID inválido.")
    return

    for d in despesas:
        if d['id'] == id_alvo:
            despesas.remove(d)
            salvar_despesas(despesas)
            print("\n Despesa removida!\n")
            return

    print("\n ID não encontrado!\n")


# ------------------- Resumos --------------------#

def resumo_total():
    despesas = carregar_despesas()
    total = sum(d['valor'] for d in despesas)

    print(f"\n💰 TOTAL GERAL GASTO: R$ {total:.2f}")
    print(f"📌 Número de despesas cadastradas: {len(despesas)}\n")

def resumo_por_mes():
    despesas = carregar_despesas()
    mes = input("Digite o mês (01-12): ")
    ano_atual = str(datetime.now().year)

    filtradas = [d for d in despesas if d['data'].startswith(f"{ano_atual}-{mes}")]

    if not filtradas:
        print("\nNenhuma despesa encontrada nesse mês.\n")
        return

    total = sum(d['valor'] for d in filtradas)

    print(f"\n Total gasto em {mes}/{ano_atual}: R$ {total:.2f}")
    print(f" Número de despesas no mês: {len(filtradas)}\n")   
  



    
# ------------------- Exportar Excel --------------------#


def exportar_para_exel():
    despesas = carregar_despesas()

    if not despesas:
        print('\nNenhuma despesa para exportar.\n')
        return
    wb = Workbook()
    ws = wb.active
    ws.title = "Despesas"

    ws.append(['ID', 'Descrição', 'Valor', 'Categoria', 'Data'])

    for d in despesas:
        ws.append([d['id'], d['descricao'], d['valor'], d['categoria'], d['data']])
    arquivo_exel = 'despesas.xlsx'
    wb.save(arquivo_exel)
    print(f"\nArquivo Excel '{arquivo_exel}' gerado com sucesso!\n")


# ------------------- Menu Principal --------------------#

def menu():
    while True:
        print("===== ORGANIZADOR DE DESPESAS =====")
        print('1 - Adicionar despesa')
        print('2 - Listar despesas')
        print('3 - Atualizar despesa')
        print('4 - Remover despesa')
        print('5 - Resumo total')
        print('6 - Resumo por mês')
        print('7 - Exportar para Excel')
        print('8 - Limpar todas as despesas')
        print('0 - Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            adicionar_despesas()
        elif opcao == '2':
            listar_despesas()
        elif opcao == '3':
            atualizar_despesa()
        elif opcao == '4':
            remover_despesa()
        elif opcao == '5':
            resumo_total()
        elif opcao == '6':
            resumo_por_mes()
        elif opcao == '7':
            exportar_para_exel()
        elif opcao == '8':
            limpar = input("Tem certeza que deseja apagar tudo? (s/n): ")
            if limpar.lower() == 's':
                salvar_despesas([])
                print("\n✔ Todas as despesas foram apagadas!\n")
        elif opcao == '0':
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida!")
menu()