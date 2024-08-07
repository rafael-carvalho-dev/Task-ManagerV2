from src import *

def main():
    introduction()
    while True:
        create_database()
        menu()
        input("Para retornar ao Menu, tecle 'Enter'.\n")


if __name__ == '__main__':
   main()