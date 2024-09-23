from psycopg2 import sql

# Busca as maquinas disponives
def fetch_idle_machines(connection):
    try:
        cursor = connection.cursor()
        query_statement = "SELECT * FROM machines_status WHERE current_status = 'idle'"
        
        query = sql.SQL(query_statement)\
        .format(table=sql.Identifier('machines_status'))
        
        cursor.execute(query)
        records = cursor.fetchall()
        
        return records
    except Exception as e:
        print(f"Ocorreu um erro na consulta do status das maquinas: {e}")    
    finally:
        # Fechar o cursor e a conexão
        if cursor:
            cursor.close()
            
# Busca proximo robo a ser executado na fila da base do lincopt
def fetch_next_bot_in_queue(connection):
    cursor = connection.cursor()
    query_statemet = "SELECT * FROM queue WHERE queue_position = 1"
    
    query = sql.SQL(query_statemet.format(table=sql.Identifier('queue')))
    
    cursor.execute(query)
    records = cursor.fetchall()
    
    return records