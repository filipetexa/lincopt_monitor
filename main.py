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
from utils.optimization_algorithms import *


# Variaveis Globais:

if __name__ == '__main__':
    while True:
        ...
        # 1. Esperando maquina ficar liberada
        client_db_connection = get_db_connection(config['rpa_database'])
        idle_machines = fetch_idle_machines(client_db_connection)
        
        
        for machine in idle_machines:
            ...
            # 2. Buscando proximo robo
            app_db_connection = get_db_connection(config['lincopt_database'])
            next_bot = fetch_next_bot_in_queue(app_db_connection)
            
            queue = fetch_all_bots_in_queue(app_db_connection)
            new_queue = queue
            
            # 3. Reorganizando fila utilizando algoritimo de ordenação.
            ...
            
            delete_all_bots_in_queue(app_db_connection)
            for bot in new_queue:
                insert_bot_in_queue(app_db_connection,queue_position=None,robot_name=None)
            
            # 4. Startando robo na maquina
            ...
        
        
        # Espera 1 segungo para os ciclos do while não serem muito rapidos durante os testes
        time.sleep(1)
        
        