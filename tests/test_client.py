import asyncio
from unittest.mock import patch
from datetime import datetime, timedelta
from math import isclose
import pytest

from client import report_programs_running


@pytest.mark.asyncio
@patch("client.send_running_programs")
async def test_request_interval(mock_send_program):
    time_register = []
    client_loop_timeout = 21
    request_interval = 5
    expect_n_calls = client_loop_timeout // request_interval + 1

    async def register_time_side_effect(_):
        time_register.append(datetime.now())

    mock_send_program.side_effect = register_time_side_effect

    expected_host = "no_host"
    try:
        await asyncio.wait_for(report_programs_running(expected_host), client_loop_timeout)
    except asyncio.exceptions.TimeoutError:
        pass
    else:
        # Fail test if exception is not thrown
        assert False

    assert len(time_register) == expect_n_calls

    for time1, time2 in zip(time_register, time_register[1:]):
        time_difference: timedelta = time2 - time1
        assert isclose(time_difference.total_seconds(), request_interval,
                       rel_tol=2e-2)  # unlikely that the interval will be exactly 5 seconds

    # check all call arguments were the expected_params
    assert all([call_.args == (expected_host,) for call_ in mock_send_program.call_args_list])
    assert mock_send_program.call_count == expect_n_calls
