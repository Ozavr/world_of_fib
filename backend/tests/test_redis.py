import pytest
import asyncio


@pytest.mark.asyncio
async def test_redis_confines_values(redis_controller):
    result = '0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040'
    data = {
        'from': 0,
        'to': 1000000
    }
    await redis_controller.set(data, result)
    redis_result = await redis_controller.get(data)
    assert redis_result.decode() == result


@pytest.mark.asyncio
async def test_redis_minimal_values(redis_controller):
    result = '0, 1, 1'
    data = {
        'from': 0,
        'to': 1
    }
    await redis_controller.set(data, result)
    redis_result = await redis_controller.get(data)
    assert redis_result.decode() == result


@pytest.mark.asyncio
async def test_redis_negative_values(redis_controller):
    result = 'test negatives values'
    data = {
        'from': -1,
        'to': -2
    }
    await redis_controller.set(data, result)
    redis_result = await redis_controller.get(data)
    assert redis_result.decode() == result


@pytest.mark.asyncio
async def test_redis_max_values(redis_controller):
    result = 'List of numbers is empty'
    data = {
        'from': 999999,
        'to': 1000000
    }
    await redis_controller.set(data, result)
    redis_result = await redis_controller.get(data)
    assert redis_result.decode() == result