from unittest.mock import Mock
from lib.time_error import TimeError


def test_time_difference_between_local_and_remote_servers():
    server_time_request = Mock()
    response = Mock()
    server_time_request.get.return_value = response
    response.json.return_value = {"unixtime": 1695983957}

    timer_mock = Mock()
    timer_mock.time.return_value = 1695983957.5
    time_error = TimeError(server_time_request, timer_mock)
    result = time_error.error()
    assert result == -0.5