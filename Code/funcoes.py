import time
import json
import os

TEMPO = 1

#Função que permiti o usuário segui no momento que achar melhor, precionando enter:
def enter_time():
    enter = input("Precione [ENTER] para continuar.\n")


#Função para limpar tela:
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_inicial():
    MENU_ASCII = """
========================================
  _______  ____         _____   ____  
 |__   __|/ __ \       |  __ \ / __ \ 
    | |  | |  | | ____ | |  | | |  | |
    | |  | |  | ||____|| |  | | |  | |
    | |  | |__| |      | |__| | |__| |
    |_|   \____/       |_____/ \____/

          [ TO-DO LIST v1.0 ]
========================================
    """
    print(MENU_ASCII)

    print(" [1] Adicionar nova tarefa")
    print(" [2] Listar todas as tarefas")
    print(" [3] Marcar tarefa como concluída")
    print(" [4] Excluir uma tarefa")
    print("----------------------------------------")
    print(" [0] Sair do sistema")
    print("========================================\n\n")

#Função para adicionar tarefas no banco de dados:
def adicionar_tarefa(descricao):
    caminho_arquivo = "Code/tasks.json"
    lista_tarefas = []

    if os.path.exists(caminho_arquivo):
        try:
            with open(caminho_arquivo, "r") as arquivo:
                lista_tarefas = json.load(arquivo)
        except json.JSONDecodeError:
            lista_tarefas = []

    nova_tarefa = {'descricao': descricao, 'concluida': False}
    lista_tarefas.append(nova_tarefa)

    with open(caminho_arquivo, "w") as arquivo:
        json.dump(lista_tarefas, arquivo, indent=4)
    
    print("Tarefa adicionada com sucesso!")
    time.sleep(TEMPO)


#Função para listar as tarefas do banco de dados:
def listar_tarefas():
    num = 1
    caminho_arquivo = "Code/tasks.json"
    lista_tarefas = []

    if os.path.exists(caminho_arquivo):
        try:
            with open(caminho_arquivo, "r") as arquivo:
                lista_tarefas = json.load(arquivo)
        except json.JSONDecodeError:
            lista_tarefas = []

    print(">>> [LISTA DE TAREFAS SALVAS] <<<")
    print(f"*** Tarefas salvas: {len(lista_tarefas)} ***")
    print("\n========================================\n")

    for item in lista_tarefas:
        print(f"> TAREFA {num}: {item['descricao']}")
        if item['concluida'] == False:
            print("> STATUS: 🔶 Em andamento")
        else:
            print("> STATUS: 🟩 Concluída")
        print("\n========================================\n")

        num += 1


#Função para iniciar a conclusão de tarefa:
def concluir_tarefa():
    caminho_arquivo = "Code/tasks.json"
    lista_tarefas = []

    if os.path.exists(caminho_arquivo):
        try:
            with open(caminho_arquivo, "r") as arquivo:
                lista_tarefas = json.load(arquivo)
        except json.JSONDecodeError:
            lista_tarefas = []

    try:
        if not lista_tarefas:
            print("Não há tarefas para concluir.")
            time.sleep(1)
        else:
            listar_tarefas()
            indice = int(input("Digite o número da tarefa que deseja concluir: "))
            
            if 1 <= indice <= len(lista_tarefas):
                lista_tarefas[indice - 1]['concluida'] = True
                with open(caminho_arquivo, "w") as arquivo:
                    json.dump(lista_tarefas, arquivo, indent=4)
                print(f"Tarefa {indice} concluída com sucesso!")
                time.sleep(TEMPO)
            else:
                print(f"Erro: A tarefa número {indice} não existe.")
                time.sleep(TEMPO)

    except ValueError:
            print("Por favor, digite um número válido.")
            time.sleep(TEMPO)
    

def excluir_tarefa():
    caminho_arquivo = "Code/tasks.json"
    lista_tarefas = []

    if os.path.exists(caminho_arquivo):
        try:
            with open(caminho_arquivo, "r") as arquivo:
                lista_tarefas = json.load(arquivo)
        except json.JSONDecodeError:
            lista_tarefas = []

    try:
        if not lista_tarefas:
            print("Não há tarefas para concluir.")
            time.sleep(1)
        else:
            listar_tarefas()
            indice = int(input("Digite o número da tarefa que deseja concluir: "))
    except ValueError:
            print("Por favor, digite um número válido.")
            time.sleep(TEMPO)

    if 1 <= indice <= len(lista_tarefas):
        lista_tarefas.pop(indice - 1)
        with open(caminho_arquivo, "w") as arquivo:
            json.dump(lista_tarefas, arquivo, indent=4)
        print(f"Tarefa {indice} excluída com sucesso!")
    else:
        print(f"Erro: A tarefa número {indice} não existe.")
        
    time.sleep(TEMPO)