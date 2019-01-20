from fib.routing import FibRouter


class Router:

    def __init__(self, app, sio, loop):
        self.app = app
        self.sio = sio
        self.loop = loop
        self.routes = [
            FibRouter
        ]
        self.init_routes()

    def init_routes(self):
        for route in self.routes:
            route(self.app, self.sio, self.loop)