"""
Script principal

Estados: 
1. Esperando maquina ficar liberada
2. Buscando proximo robo
3. Reorganizando fila utilizando algoritimo de ordenação.
4. Startando robo na maquina

"""
import time
import asyncio
from config import config
from database.connection import get_db_connection
from database.queries import *
from utils.optimization_algorithms import *
from utils.utils import *
from copy import deepcopy
import subprocess

async def main():
    client_db_connection = get_db_connection(config['rpa_database'])
    while True:
        print('Nenhuma maquina disponível')
        # 1. Esperando maquina ficar liberada
        idle_machines = fetch_idle_machines(client_db_connection)
        
        for machine in idle_machines:
            print(f'Maquina disponivel: {machine[1]}')
            # 2. Buscando proximo robo
            app_db_connection = get_db_connection(config['lincopt_database'])
            next_bot = fetch_next_bot_in_queue(app_db_connection)
            
            
            # 3. Reorganizando fila utilizando algoritimo de ordenação.
            queue = fetch_all_bots_in_queue(app_db_connection)
            new_queue = reorganize_queue_FIFO(queue)
            
            delete_all_bots_in_queue(app_db_connection)
            for bot in new_queue:
                insert_bot_in_queue(app_db_connection,queue_position=bot[0],robot_name=bot[1])
            
            # 4. Startando robo na maquina
            asyncio.create_task(start_bot(machine[1], next_bot[0][1], '60'))
        
        # Espera 1 segungo para os ciclos do while não serem muito rapidos durante os testes
        await asyncio.sleep(2)
        
        
if __name__ == '__main__':
    asyncio.run(main())
        