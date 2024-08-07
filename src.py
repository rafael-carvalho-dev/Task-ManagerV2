import os
import sqlite3
import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import print


def create_database():
    """
    Cria o banco de dados e a tabela de tarefas, se não existirem.
    """
    with sqlite3.connect('tasks.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS TAREFAS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descrição TEXT NOT NULL,
                concluída BOOLEAN NOT NULL CHECK (concluída IN (0, 1))
            )
        ''')
        conn.commit()


def create_task():
    """
    Solicita ao usuário o nome e a descrição da tarefa e a insere na banco de dados.
    """
    new_task = input('\nEscreva o nome da Tarefa: ')
    describe_task = input('Escreva a descrição da Tarefa: ')
    
    with sqlite3.connect('tasks.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO TAREFAS (nome, descrição, concluída) VALUES (?, ?, ?)', (new_task, describe_task, 0))
        conn.commit()


def view_tasks():
    """
    Exibe todas as tarefas armazenadas no banco de dados em uma tabela formatada.
    """
    with sqlite3.connect('tasks.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, nome, descrição, concluída FROM TAREFAS')
        tasks = cursor.fetchall()

    console = Console()
    table = Table(title='Tarefas')
    table.add_column('ID', justify='left', style='cyan', no_wrap=True)
    table.add_column('Nome', justify='left', style='cyan', no_wrap=True)
    table.add_column('Descrição', justify='left', style='cyan', no_wrap=True)
    table.add_column('Status', justify='left', style='cyan', no_wrap=True)

    for task in tasks:
        id, nome, descrição, concluída = task
        status = '[green]Concluída :white_check_mark:[/green]' if concluída == 1 else '[red]Pendente[/red]'
        table.add_row(str(id), nome, descrição, status)

    console.print(table)


def mark_task_as_completed():
    """
    Solicita ao usuário o ID da tarefa a ser marcada como concluída e atualiza seu
    status no banco de dados.
    """
    id = input('\nDigite o id da tarefa a ser marcada como concluída: ')

    with sqlite3.connect('tasks.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE TAREFAS SET concluída = ? WHERE id = ?', (1, id))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Tarefa de ID '{id}' concluída!")
        else:
            print(f"Nenhuma tarefa encontrada com o ID '{id}'.")


def delete_task():
    """
    Solicita ao usuário o ID da tarefa a ser excluída e a remove do banco de dados.
    """
    id = input('\nDigite o id da tarefa a ser excluída: ')

    with sqlite3.connect('tasks.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM TAREFAS WHERE id = ?', (id,))
        conn.commit()


def quit_program():
    """
    Exibe uma mensagem de saída e encerra o programa.
    """
    print('\nSaindo...\n')
    sys.exit()


def clear_console():
    """
    Limpa o console, dependendo do sistema operacional.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    """
    Exibe o menu de opções e executa a ação correspondente com base na escolha do usuário.
    """
    console = Console()
    console.print('[bold] Escolha uma das opções:\n\n[1] Criar uma Tarefa\n\[2] Visualizar Tarefas\n[3] Marcar Tarefa como concluída\n\[4] Excluir Tarefa\n[5] Sair\n[/]')
    choice = input('')
    
    options = {
        '1': create_task,
        '2': view_tasks,
        '3': mark_task_as_completed,
        '4': delete_task,
        '5': quit_program
    }

    action = options.get(choice)
    if action:
        clear_console()
        action()
    else:
        print('Opção inválida. Tente novamente.')


def introduction():
    """
    Exibe a introdução do programa com um painel estilizado.
    """
    console = Console()
    title = 'Gerenciador de Tarefas'
    title_text = Text(title, justify='center', style='bold yellow')
    panel = Panel(title_text, title_align='center', border_style='green', width=40)
    console.print(panel)
    print('\n')
