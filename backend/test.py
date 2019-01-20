from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from aiohttp import web
import asyncio
import signal


class MyAppTestCase(AioHTTPTestCase):

    async def get_application(self):

        def handler_loop(loop):
            loop.remove_signal_handler(signal.SIGTERM)
            loop.stop()

        def init_event_loop(app):
            loop = asyncio.get_event_loop()
            try:
                loop.add_signal_handler(signal.SIGTERM, lambda loop : handler_loop(loop), loop)
            except:
                pass

        app = web.Application()
        init_event_loop()
        
        
        return app