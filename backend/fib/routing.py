from .controllers.sockets import FibSocket


class FibRouter:
    def __init__(self, app, sio, loop):
        self.app = app
        self.sio = sio
        self.loop = loop
        self.sockets = [
            FibSocket
        ]
        self.init_sockets()

    def init_sockets(self):
        for socket in self.sockets:
            socket(self.app, self.sio, self.loop)