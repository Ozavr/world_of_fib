import sys, os 
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/..")) 


import pytest
import asyncio
import aioredis
import os
from settings import REDIS
from fib.controllers.data import RedisController
from fib.controllers.validation import FibValidator
from fib.controllers.views import FibView


@pytest.fixture()
def event_loop():
    loop = asyncio.get_event_loop()
    return loop


@pytest.fixture()
async def redis(event_loop):
    redis = await aioredis.create_redis(
            (REDIS['host'], REDIS['port']), 
            db=REDIS['db'], loop=event_loop)
    return redis


@pytest.fixture()
async def redis_controller(redis):
    class App:
        redis = None
    app = App()
    app.redis = redis
    redis_controller = RedisController(app)
    # yield redis_controller
    return redis_controller


@pytest.fixture()
async def validator_controller():
    controller = FibValidator()
    return controller


@pytest.fixture()
async def view_controller(redis, event_loop):
    class App:
        redis = None
    app = App()
    app.redis = redis
    sio = None
    view_controller = FibView(app, sio, event_loop)
    return view_controller
    