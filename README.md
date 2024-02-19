# Simulación de un Call Center con Atención de Tickets

## Descripción
    Estás liderando el desarrollo de un sistema de simulación de un call center que gestionará la atención de un número determinado de tickets de forma eficiente. El sistema debe asignar tickets a N agentes de forma paralela y registrar tanto el momento de la asignación del ticket como el momento de la finalización de la atención del mismo en un archivo CSV.

## Pasos para correr

```
    pip install -r .\requirements.txt
    py -m uvicorn main:app --reload
    
    Ir a la ruta http://127.0.0.1:8000/docs#/
    
    Cargar el dataset csv en la sección Uploads (El dataset de prueba está precargado)
    /start_fixed_sims/ para correr las simulaciones con 3, 5 y 10 agentes
    /start_sim/ para correr la simulación la cantidad de agentes deseado
        Retorna el csv de los resultados, se puede desacargar
        Se puede llamar directamente la ruta http://127.0.0.1:8000/run_sim/?agents=3 para obtener el csv como descarga

    Ir a la carpeta reports para ver los resultados
```



## Objetivos
    Asignar tickets entre N agentes. 
        Manejo de colas como mecanismo de asignación de tickets
    Registrar los tiempos de atención de los tickets.
        Registrar tiempo en que se toma el ticket
        Registrar tiempo en el que se completa el ticket
        Registrar el agente que atendió el tiquet
    Simular atención de tickets 
        Cada agente debe operar de forma paralela 
        Se asume tiempo aleatorio entre 2 y 3 secs de atención
    Sistema de monitoreo
        Archivo CSV que en el que se puede ir observando el progreso de guardado de los registros de atención
    
    (Optional) No se espera un UI, optional - a real-time way to track progress
    (Optional) Record/Track changes on a DB
    (Optional) API para cargar datasets
    (Optional) API para correr simulaciones



## Definiciones
    Python 3.11
    FastAPI
    Pydantic
    
## Iteraciones
###     Iteración1: 
        Proveer archivo de prueba como ruta estática. 
        Asumir que el archivo está correcto, es decir que todas las filas tienen datos correctos.
        Correr simulación según orden de llegada
        Si la hora de creación es la misma ordenar por prioridad
        Escribir archivo estático de resultados. 
        Con el fin de realizar mejoras en las siguientes iteraciones se correrá a modo de api.

###    Iteración 2: 
        El archivo de resultados tiene como prefijo la fecha y hora a la que se inició la simulación. 
        Se puede correr una simulación con un número custom de agentes.
        Se genera servicio para cargar los datasets .
        Se genera un endpoint para generar los 3 casos planteados en el enunciado, corre simulaciones con 3, 5, 10 agentes.
        Solamente se guardará el último dataset que se cargue. Se llamará tickets_dataset.csv y será guardado en la carpeta uploads
        Los reportes serán guardados en la carpeta reports

## 