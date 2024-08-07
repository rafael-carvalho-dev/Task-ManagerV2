import os
import sys
from cx_Freeze import setup, Executable

# Dependências adicionais
build_exe_options = {
    "packages": ["os", "sqlite3", "sys"],
    "include_files": [],
    "build_exe": "build/exe.linux-x86_64-3.x",  # Diretório de saída
}

# Base é "Win32GUI" para GUI no Windows ou None para console no Linux
base = None

config = [
    Executable("main.py", base=base, target_name="gerenciador_tarefas")
]

setup(
    name="TaskManager",
    version="2.0",
    description="Gerenciador de Tarefas",
    author="Rafael Carvalho",
    options = {"build_exe": build_exe_options},
    executables=config
)