class RedisController:
    def __init__(self, app):
        self.redis = app.redis

    async def get(self, data):
        key = self.generate_key(data)
        data = await self.redis.get(key)
        return data

    async def set(self, data, result):
        key = self.generate_key(data)
        await self.redis.set(key, result)

    def generate_key(self, data):
        key = f'{data["from"]}-{data["to"]}'
        return key