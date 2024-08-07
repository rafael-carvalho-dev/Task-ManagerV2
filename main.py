from src import *

def main():
    """
    Essa função inicia o programa. Ela mostra ao usuário
    como usar o sistema, cria um banco de dados e exibe um menu
    até que o usuário saia.
    """
    introduction()
    while True:
        create_database()
        menu()
        input("Para retornar ao Menu, tecle 'Enter'.\n")


if __name__ == '__main__':
   main()