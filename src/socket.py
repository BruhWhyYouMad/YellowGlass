import websocket
from threading import Thread

class Sockets():
    def __init__(self, receive, handler):
        self.host = "ws://127.0.0.1"
        self.receive = receive
        self.handler = handler
    
    def start(self):
        thread = Thread(target=self.connect)
        thread.daemon = True
        thread.start()

    def connect(self):
        self.wsapp = websocket.WebSocketApp(
                self.host,
                on_message=self.on_message,
        )
        self.wsapp.run_forever()

    def on_message(self, ws, raw):
        self.handler(raw, self.receive)

    def send_message(self, message):
        self.wsapp.send(message)
