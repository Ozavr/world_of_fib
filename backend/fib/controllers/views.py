from .validation import FibValidator
from .data import RedisController
from .calculates import FibController


class FibView:
    def __init__(self, app, sio, loop):
        self.app = app
        self.sio = sio
        self.loop = loop
        self.validator = FibValidator()
        self.redis_controller = RedisController(self.app)
        self.fib_controller = FibController()

    async def run(self, data):
        validate_status = self.validator.run(data)
        if validate_status:
            results = await self.get_result_data(data)
        else:
            results = 'Your data invalid'
        return results

    async def get_result_data(self, data):
        result = await self.redis_controller.get(data)
        if not result:
            result = await self.calculate_result(data)
        else:
            result = result.decode()
        return result

    async def calculate_result(self, data):
        result = self.fib_controller.calculate(data)
        self.loop.create_task(self.redis_controller.set(data, result))
        return result

    

