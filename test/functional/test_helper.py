import os
import socket
from time import sleep
from typing import Callable


class NoAvailablePortError(Exception):
    pass


def get_available_from_port_range(from_port: int, to_port: int) -> int:
    """Returns available local port number.

    Args:
        from_port: The start port to search
        to_port: The end port to search

    Returns:
        int: available local port number which are found first

    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for port in range(from_port, to_port):
        try:
            if sock.connect_ex(('localhost', port)) != 0:
                return port
        finally:
            sock.close()

    raise NoAvailablePortError(f'No available port between {from_port} and {to_port}')


def is_ci() -> bool:
    """Returns if current execution is running on CI

    Returns:
        `True` if current executions is on CI
    """
    return os.getenv('CI', 'false') == 'true'


def wait_for(method: Callable, timeout: int) -> bool:
    """Wait for `method` True

    Args:
        method: The target method to be waited. Need to return `bool`
        timeout: The timeout to be waited (sec.)

    Returns:
        bool: True if `method` returns True

    """
    for i in range(timeout + 1):
        if method():
            break
        if i == timeout:
            return False
        sleep(1)
    return True
