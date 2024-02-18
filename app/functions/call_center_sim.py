import asyncio
from app.utils.date_util import get_today_str

import aiofiles

from app.functions import sort_tickets, load_tickets, queue_tickets, process_ticket


async def run_sim(agents: int):
    """Run the call center simulation"""
    # cargar los tickets
    tickets = await load_tickets("tickets_dataset.csv")
    # ordenar los tickets, según los parámetros elegidos
    tickets = await sort_tickets(tickets)
    q = await queue_tickets(tickets)

    report_file_name = f"{get_today_str()}_simulacion_{agents}_agentes_{len(tickets)}_casos.csv"
    async with aiofiles.open(report_file_name, 'a') as csvfile:
        await csvfile.write("id,fecha_creacion, prioridad, agente, fecha_asignacion, fecha_resolucion\n")
    # semaphore para controlar el numero de tickets que se pueden ejecutar al tiempo
    semaphore = asyncio.Semaphore(agents)

    # el número de agent_processes viene dado por el numero de agentes que se van a simular
    agent_processes = [agent_process(report_file_name, i, q, semaphore) for i in range(agents)]

    await asyncio.gather(*agent_processes)
    await q.join()
    return report_file_name


async def agent_process(filename, agent_id: int, q: asyncio.Queue, semaphore: asyncio.Semaphore):
    """Agent process"""
    while not q.empty():
        async with semaphore:
            try:
                ticket = await q.get()
                if ticket is None:
                    break
                await process_ticket(filename, ticket, agent_id+1)
            except asyncio.QueueEmpty:
                return
            finally:
                q.task_done()
