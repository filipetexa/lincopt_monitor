import asyncio

async def start_bot(machine, bot_name, wait_time):
    print(f"Attempting to start bot {bot_name} on machine {machine}")
    process = await asyncio.create_subprocess_exec(
        'python3', 'scripts/start_bot.py', machine, bot_name, wait_time,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    
    if process.returncode == 0:
        print(f'Success: Bot {bot_name} started on machine {machine}')
    else: 
        print(f'Error: Failed to start bot {bot_name} on machine {machine}, error: {stderr.decode()}')

def list_of_tuple_to_list_of_lists(tupple_list):
    list_of_lists = []
    for tupple in tupple_list:
        new_list = list(tupple)
        list_of_lists.append(new_list)
        
    return list_of_lists


