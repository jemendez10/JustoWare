from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def tarea_programada():
    print("¡La tarea se está ejecutando en:", datetime.now(), "!")

# Crear un objeto de planificación
scheduler = BlockingScheduler()

# Programar la tarea para que se ejecute cada 1 minuto
scheduler.add_job(tarea_programada, 'interval', minutes=1)

try:
    print("Presiona Ctrl+C para detener la ejecución.")
    # Iniciar la ejecución del planificador
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    # Manejar la interrupción del teclado o salida del sistema
    print("La ejecución del programa ha sido interrumpida.")