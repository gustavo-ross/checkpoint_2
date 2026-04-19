import json
import time
import os

from funcoes import enter_time
from funcoes import listar_tarefas
from funcoes import adicionar_tarefa
from funcoes import limpar_tela
from funcoes import concluir_tarefa


while True:
    limpar_tela()
    print("--- TO-DO LIST ---")
    print("Selecione uma das opções abaixo.\n")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("0 - Sair\n")

    opcao = input("Digite a opção: ")

    match opcao:
        case "1":
            limpar_tela()
            descricao = input("Digite a descrição da tarefa:\n")
            adicionar_tarefa(descricao)

        case "2":
            limpar_tela()
            listar_tarefas()
            enter_time()
        
        case "3":
            limpar_tela()
            concluir_tarefa()
        
        case "0":
            limpar_tela()
            print("Finalizando TO-DO LIST...")
            break
        
        case _:
            limpar_tela()
            print("ERRO: Opção inválida.")

