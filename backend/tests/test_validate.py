import pytest
import asyncio


@pytest.mark.asyncio
async def test_validator_normal_values(validator_controller):
    data = {'from': 0, 'to': 1000000}
    status = validator_controller.run(data)
    assert status == True


@pytest.mark.asyncio
async def test_validator_negative_from(validator_controller):
    data = {'from': -1, 'to': 1000000}
    status = validator_controller.run(data)
    assert status == False


@pytest.mark.asyncio
async def test_validator_biggermaximum_from(validator_controller):
    data = {'from': 0, 'to': 1000001}
    status = validator_controller.run(data)
    assert status == False


@pytest.mark.asyncio
async def test_validator_another_type(validator_controller):
    data = {'from': 'a', 'to': 'b'}
    status = validator_controller.run(data)
    assert status == False


@pytest.mark.asyncio
async def test_validator_frombigger(validator_controller):
    data = {'from': 2, 'to': 1}
    status = validator_controller.run(data)
    assert status == False