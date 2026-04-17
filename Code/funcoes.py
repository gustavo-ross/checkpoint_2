import time
import os

lista_tarefas = []
TEMPO = 1

def enter_time():
    enter = input("Precione [ENTER] para continuar.\n")


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def adicionar_tarefa(descricao):
    lista_tarefas.append({'descricao': descricao, 'concluida': False})
    print("Tarefa adicionada com sucesso!")
    time.sleep(TEMPO)


def listar_tarefas():
    num = 1

    print("--- LISTA DE TAREFAS SALVAS ---")
    print(f"Tarefas salvas: {len(lista_tarefas)}")
    print("\n------------------------------------------------------------------------\n")

    for item in lista_tarefas:
        print(f"TAREFA {num}: {item['descricao']}")
        if item['concluida'] == False:
            print("STATUS: 🔶 Em andamento")
        else:
            print("STATUS: 🟩 Concluída")
        print("\n------------------------------------------------------------------------\n")

        num += 1


def concluir_tarefa(indice):
    limpar_tela()
    
    if 1 <= indice <= len(lista_tarefas):
        lista_tarefas[indice - 1]['concluida'] = True
        print(f"Tarefa {indice} concluída com sucesso!")
    else:
        print(f"Erro: A tarefa número {indice} não existe.")
    
    time.sleep(TEMPO)
    