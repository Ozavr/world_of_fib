import pytest
import asyncio


@pytest.mark.asyncio
async def test_view_confines_values(view_controller):
    result = '0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040'
    data = {
        'from': 0,
        'to': 1000000
    }
    compl_result = await view_controller.run(data)
    assert compl_result == result


@pytest.mark.asyncio
async def test_view_negative_from(view_controller):
    data = {'from': -1, 'to': 1000000}
    optimal_result = 'Your data invalid'
    result = await view_controller.run(data)
    assert result == optimal_result


@pytest.mark.asyncio
async def test_view_biggermaximum_from(view_controller):
    data = {'from': 0, 'to': 1000001}
    optimal_result = 'Your data invalid'
    result = await view_controller.run(data)
    assert result == optimal_result


@pytest.mark.asyncio
async def test_view_another_type(view_controller):
    data = {'from': 'a', 'to': 'b'}
    optimal_result = 'Your data invalid'
    result = await view_controller.run(data)
    assert result == optimal_result


@pytest.mark.asyncio
async def test_view_frombigger(view_controller):
    data = {'from': 2, 'to': 1}
    optimal_result = 'Your data invalid'
    result = await view_controller.run(data)
    assert result == optimal_result


@pytest.mark.asyncio
async def test_view_notresult(view_controller):
    data = {'from': 999999, 'to': 1000000}
    optimal_result = 'List of numbers is empty'
    result = await view_controller.run(data)
    assert result == optimal_result