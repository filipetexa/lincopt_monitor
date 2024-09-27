# This script will simulate a start of a bot, by interacting with the database.

import sys
import psycopg2
import time


# CONFIGURAÇÃO DO BANCO DE DADOS.
CONFIG = {
    'host' : '172.25.69.126',
    'port' : 5432,
    'user' : 'postgres',
    'password' : 'postgres',
    'database' : 'rpa_client_db'}

"""
Obs: Essa configuração esta sendo passada hardcoded porque na pratica esse script esta
simulando uma aplicação que simplesmente ira chamar o executavel de um outro serviço
que ja esta conectado com a base de dados real, ou seja, esse script no caso de um projeto
real não vai precisar interagir com o banco diretamente.
"""


# Cria uma conexão psycopg2
def get_db_connection(config):
    connection = psycopg2.connect(
        host=config['host'],
        port=config['port'],
        user=config['user'],
        password=config['password'],
        database=config['database']
    )
    return connection


def update_machine_status(machine_name, machine_status):
    connection = get_db_connection(CONFIG)
    try:
        cursor = connection.cursor()
        query_statement = f"""
        UPDATE machines_status
        SET current_status = '{machine_status}'
        WHERE machine_name = '{machine_name}'
        """

        cursor.execute(query_statement)
        connection.commit()  # Confirmando a transação no banco de dados

    except Exception as e:
        print(f"Ocorreu um erro ao atualizar o status da maquina {machine_name} para {machine_status}: {e}")    
    finally:
        # Fechar o cursor e a conexão
        if cursor:
            cursor.close()

    

if __name__ == "__main__":
    # Busca argumentos da linha de comando
    machine = sys.argv[1]
    bot = sys.argv[2]
    wait_time = int(sys.argv[3])
    
    # Atualiza status da maquina para active
    update_machine_status(machine, 'active')
    # Espera o tempo
    time.sleep(wait_time)
    # Atualiza status da maquina para idle
    update_machine_status(machine, 'idle')
