import socketio
from .views import FibView


class FibSocket:
    def __init__(self, app, sio, loop):
        self.namespace = '/fib'
        self.view = FibView(app, sio, loop)

        @sio.on('connect', namespace=self.namespace)
        async def connect(sid, environ):
            print('connect', sid)

        @sio.on('disconnect', namespace=self.namespace)
        def disconnect(sid):
            print('disconnect ', sid)

        @sio.on('calculate_fib', namespace=self.namespace)
        async def calculate_fib(sid, data):
            response = await self.view.run(data)
            await sio.emit('get_result', response, namespace=self.namespace)