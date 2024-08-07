# Gerenciador de Tarefas

Este é um aplicativo simples de linha de comando para gerenciar tarefas usando SQLite e a biblioteca `rich` para uma saída colorida e estilizada no console.

## Funcionalidades

- **Criar Tarefa**: Adicione novas tarefas com nome e descrição.
- **Visualizar Tarefas**: Veja todas as tarefas, incluindo seu status (concluída ou pendente).
- **Marcar Tarefa como Concluída**: Atualize o status de uma tarefa para concluída.
- **Excluir Tarefa**: Remova tarefas do banco de dados.
- **Interface Limpa**: Use a biblioteca `rich` para uma interface de console mais agradável.

## Instalação

### Pré-requisitos

- Python 3.7 ou superior
- SQLite

### Passos para Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/gerenciador-de-tarefas.git
    cd gerenciador-de-tarefas
    ```


2. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

3. Execute o programa:

Clique com o botão direito no script run_gerenciador_tarefas e escolha `run as a program`

## Uso

Ao executar o programa, você verá um menu com opções. Escolha uma das opções para criar, visualizar, marcar como concluída ou excluir tarefas.

## Estrutura do Projeto

```plaintext
gerenciador-de-tarefas/
│
build/
└── exe.linux-x86_64-3.x/
    ├── gerenciador_tarefas
    └── run_gerenciador_tarefas.sh
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── tasks.db
```

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.
