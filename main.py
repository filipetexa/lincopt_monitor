"""
Script principal

Estados: 
1. Esperando maquina ficar liberada
2. Buscando proximo robo
3. Reorganizando fila utilizando algoritimo de ordenação.
4. Startando robo na maquina

"""
import time
from config import config
from database.connection import get_db_connection
from database.queries import *



# Variaveis Globais:

if __name__ == '__main__':
    while True:
        ...
        # 1. Esperando maquina ficar liberada
        connection = get_db_connection(config['rpa_database'])
        
        idle_machines = fetch_idle_machines(connection)
        
        print(records)
        
        # 2. Buscando proximo robo
        # 3. Reorganizando fila utilizando algoritimo de ordenação.
        # 4. Startando robo na maquina
        
        
        # Espera 1 segungo para os ciclos do while não serem muito rapidos durante os testes
        time.sleep(1)
        
        