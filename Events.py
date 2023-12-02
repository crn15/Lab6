class EventManager:
    def __init__(self):
        
        # Se inicializa un diccionario que almacena los suscriptores de eventos.
        self.subscribers = {}

    def subscribe(self, event, callback):
        # Condiconal que agrega un callback como suscriptor al evento dado.
        # Si este evento no existe en el diccionario, se agrega con una lista vacía.
        if event not in self.subscribers:
            self.subscribers[event] = []
            
        # Se agrega el callback a la lista de suscriptores del evento.
        self.subscribers[event].append(callback)

    def unsubscribe(self, event, callback):
        # Se elimina un callback específico como suscriptor del evento dado.
        # Se verifica que el evento exista y que el callback esté en la lista de suscriptores.
        if event in self.subscribers and callback in self.subscribers[event]:
            self.subscribers[event].remove(callback)

    def notify(self, event, data=None):
        # Se verifica que haya suscriptores y se les notifica el evento.
        if event in self.subscribers:
            for callback in self.subscribers[event]:
                callback(data)
