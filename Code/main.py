import json
import time
import os

from funcoes import enter_time
from funcoes import listar_tarefas
from funcoes import adicionar_tarefa
from funcoes import limpar_tela
from funcoes import concluir_tarefa
from funcoes import excluir_tarefa
from funcoes import menu_inicial


while True:
    limpar_tela()
    menu_inicial()

    opcao = input("Digite a opção: ")

    match opcao:
        case "1":
            limpar_tela()
            print(">>> [ ADICIONAR TAREFA ] <<<")
            descricao = input("Digite a descrição da tarefa:\n--> ")
            adicionar_tarefa(descricao)

        case "2":
            limpar_tela()
            listar_tarefas()
            enter_time()
        
        case "3":
            limpar_tela()
            concluir_tarefa()

        case "4":
            limpar_tela()
            excluir_tarefa()
        
        case "0":
            limpar_tela()
            print("Finalizando TO-DO LIST...")
            break
        
        case _:
            limpar_tela()
            print("\n\n")
            print("  ========================================")
            print("     Obrigado por usar o TO-DO LIST!")
            print("     Finalizando o sistema... Até logo.")
            print("  ========================================")
            print("\n\n")
            break

