# Documentación del Sistema de Simulación de Call Center

## Descripción

Este documento describe el desarrollo de un sistema de simulación de un call center diseñado para la gestión eficiente de tickets. El sistema asigna tickets a un número determinado de agentes de manera paralela y registra eventos de atención en un archivo CSV.

## Pasos para Ejecutar

1. **Instalar los Paquetes Requeridos:**

    ```
    pip install -r .\requirements.txt
    ```

2. **Iniciar la Aplicación:**

    ```
    py -m uvicorn main:app --reload
    ```

3. **Acceder a la Interfaz de Swagger:**

    Navega a [http://127.0.0.1:8000/docs#/](http://127.0.0.1:8000/docs#/) para subir datasets y ejecutar simulaciones.

4. **Subir el Dataset CSV:**

    La sección de Uploads permite la carga de datasets CSV. Un dataset de prueba está precargado para conveniencia.

5. **Ejecutar Simulaciones Fijas:**

    Utiliza el endpoint `/start_fixed_sims/` para ejecutar simulaciones con 3, 5 y 10 agentes.

6. **Ejecutar Simulaciones Personalizadas:**

    El endpoint `/start_sim/` permite ejecutar simulaciones con un número personalizado de agentes. Accede directamente a [http://127.0.0.1:8000/run_sim/?agents=3](http://127.0.0.1:8000/run_sim/?agents=3) para descargar los resultados CSV.

7. **Ver Resultados:**

    Revisa la carpeta `reports` para ver los resultados de las simulaciones.

## Objetivos

- **Asignación de Tickets:** Utilizar colas para la asignación eficiente de tickets a los agentes.
- **Registro de Eventos:** Registrar el momento en que se toma un ticket, el momento en que se completa, y el agente que atendió el ticket.
- **Simulación de Atención de Tickets:** Operar cada agente de forma paralela, asumiendo un tiempo aleatorio de atención entre 2 y 3 segundos.
- **Sistema de Monitoreo:** Utilizar un archivo CSV para observar el progreso de los registros de atención.


## Características Opcionales

- Monitoreo en tiempo real del progreso (no se requiere UI).
- Registro/seguimiento de cambios en una base de datos.
- API para la carga de datasets.
- API para ejecutar simulaciones.
- Sistema de administración de datasets para permitir el manejo de datasets para diferentes simulaciones.

## Definiciones

- **Versión de Python:** 3.11
- **Frameworks:** FastAPI, Pydantic

## Iteraciones

### Iteración 1

- Proveer un archivo de prueba mediante una ruta estática.
- Asumir que el archivo es correcto, es decir, todas las filas tienen datos válidos.
- Ejecutar simulaciones basadas en el orden de llegada.
- Si los tiempos de creación son idénticos, ordenar por prioridad.
- Escribir los resultados en un archivo estático.
- Utilizar un modo API para mejoras futuras.

### Iteración 2

- Nombrar el archivo de resultados con la fecha y hora en que se inició la simulación.
- Permitir simulaciones con un número personalizado de agentes.
- Implementar un servicio para la carga de datasets.
- Crear un endpoint para los casos especificados (3, 5, 10 agentes).
- Solo se guardará el último dataset cargado, nombrado `tickets_dataset.csv`, en la carpeta `uploads`.
- Los informes se guardarán en la carpeta `reports`.
 ##