import asyncio
import aioredis
import socketio
import signal
from aiohttp import web
from settings import REDIS, SERVER
from routing import Router


class WorldOfFib:
    def __init__(self):
        self.app = web.Application()
        self.init_event_loop()
        self.loop.run_until_complete(self.get_redis())
        self.init_socketio()
        self.init_routing()
        self.register_shutdown()
        self.start()

    def init_event_loop(self):
        self.loop = asyncio.get_event_loop()
        try:
            self.loop.add_signal_handler(signal.SIGTERM, self.handler_loop, self.loop)
        except:
            pass

    def handler_loop(self):
        self.loop.remove_signal_handler(signal.SIGTERM)
        self.loop.stop()

    async def get_redis(self):
        redis = await aioredis.create_redis(
            (REDIS['host'], REDIS['port']), 
            db=REDIS['db'], loop=self.loop)
        self.app.redis = redis

    def init_socketio(self):
        self.sio = socketio.AsyncServer(async_mode='aiohttp')
        self.sio.attach(self.app)

    def init_routing(self):
        Router(self.app, self.sio, self.loop)

    def register_shutdown(self):
        self.app.on_shutdown.append(self.close_redis)

    def close_redis(self, app):
        app.redis.close()

    def start(self):
        web.run_app(self.app, host=SERVER['host'], port=SERVER['port'])


if __name__ == '__main__':
    app = WorldOfFib()