from copy import deepcopy

def reorganize_queue_FIFO(queue):
    ...
    # Ordena fila pela posições atuais
    queue.sort(key=lambda bot: bot[0])
    
    first_item =  queue.pop(0)
    queue.append(first_item)
    
    # Rescrever as posiçoes
    for i, item in enumerate(queue):
        ...
        queue[i][0] = i + 1

    return queue
