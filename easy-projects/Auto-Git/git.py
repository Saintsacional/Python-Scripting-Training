import os
import subprocess
import re

def get_last_version():
    """Obtém a última versão do commit a partir do histórico do Git."""
    try:
        # Executa o comando git log para obter os últimos commits
        log_output = subprocess.check_output(["git", "log", "--oneline"], text=True)
        
        # Encontra o último commit que contém "projecto v-X"
        match = re.search(r"projecto v-(\d+)", log_output)
        
        if match:
            return int(match.group(1))  # Retorna o número da versão como inteiro
        else:
            return 0  # Se não encontrar, começa do zero
    except subprocess.CalledProcessError:
        return 0

def make_commit():
    """Faz commit e push com a versão incrementada."""
    last_version = get_last_version()
    new_version = last_version + 1  # Incrementa a versão

    commit_message = f"projecto v-{new_version}"

    print(f"📌 Fazendo commit: {commit_message}")

    try:
        # Executa os comandos Git
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
        
        print(f"✅ Commit {commit_message} feito com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar comandos Git: {e}")

if __name__ == "__main__":
    make_commit()
