# 📝 To-Do List

Uma aplicação simples e eficiente de Lista de Tarefas (To-Do List), desenvolvida em Python. O projeto permite gerenciar tarefas diárias com persistência de dados em formato JSON.

## 🚀 Funcionalidades

- **Adicionar Tarefa:** Permite inserir uma nova descrição para uma atividade.
- **Listar Tarefas:** Exibe todas as tarefas salvas, indicando se estão "Em andamento" ou "Concluídas".
- **Concluir Tarefa:** Altera o status de uma tarefa específica para concluída.
- **Excluir Tarefa:** Remove permanentemente uma tarefa da lista.
- **Persistência de Dados:** Todas as tarefas são salvas em um arquivo `tasks.json`, garantindo que os dados não sejam perdidos ao fechar o programa.

## 🛠️ Tecnologias Utilizadas

- **Python 3.14**
- **JSON:** Para armazenamento de dados.
- **OS & Time:** Bibliotecas nativas para manipulação do sistema e controle de fluxo.

## 📁 Estrutura do Projeto

```text
├── main.py          # Arquivo principal que executa o loop do menu
├── funcoes.py       # Módulo contendo a lógica e as funções do sistema
└── Code/
    └── tasks.json   # Banco de dados em formato JSON (gerado automaticamente)
```

## 🖥️ Demonstração do Menu

Ao iniciar o programa, você verá uma interface ASCII organizada:
```text
========================================
  _______  ____         _____   ____  
 |__   __|/ __ \       |  __ \ / __ \ 
    | |  | |  | | ____ | |  | | |  | |
    | |  | |  | ||____|| |  | | |  | |
    | |  | |__| |      | |__| | |__| |
    |_|   \____/       |_____/ \____/

          [ TO-DO LIST v1.0 ]
========================================
 [1] Adicionar nova tarefa
 [2] Listar todas as tarefas
 [3] Marcar tarefa como concluída
 [4] Excluir uma tarefa
----------------------------------------
 [0] Sair do sistema
========================================
```

## 📝 Notas de Versão (v1.0)
- O sistema utiliza `cls` (Windows) ou `clear` (Linux/Mac) para manter a interface limpa.
- O tratamento de erros básico para entradas de usuário (Validação de números inteiros).

---
Desenvolvido por Gustavo-Ross