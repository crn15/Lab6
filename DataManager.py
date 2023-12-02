import time
import random
from Events import EventManager

class RealTimeDataManager:
    def __init__(self):
        
        # Se inicializan datos de temperatura y humedad.
        self.data = {"temperatura": 25.0, "humedad": 60.0}
        
        # Instancia de EvnetManager.
        self.event_manager = EventManager()

    def start_real_time_updates(self):
        
        # Ciclo para actualizaciones en tiempo real.
        while True:
            
            # Espera 3 segundos y genera datos.
            time.sleep(3)
            self.generate_real_time_data()
            
            # Notifica a través del EventManager que los datos han cambiado
            self.event_manager.notify("datos_actualizados", self.data)

    def generate_real_time_data(self):
        self.data["temperatura"] += random.uniform(-1.0, 1.0)
        self.data["humedad"] += random.uniform(-2.0, 2.0)

# Instancia de RealTimeDataManager
real_time_data_manager = RealTimeDataManager()

# Función callback que imprime los datos actualizados.
def print_updated_data(data):
    print(f"Datos actualizados en tiempo real: {data}")

# Suscribe el callback al EventManager.
real_time_data_manager.event_manager.subscribe("datos_actualizados", print_updated_data)

# Actualizaciones en tiempo real en segundo plano.
import threading
update_thread = threading.Thread(target=real_time_data_manager.start_real_time_updates)
update_thread.start()

# Mantiene el programa principal en espera.
try:
    while True:
        time.sleep(1)
        
except KeyboardInterrupt:
    # Maneja interrupción.
    print("\nPrograma terminado.")
