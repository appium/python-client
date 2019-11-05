import os
import socket


class NoAvailablePortError(Exception):
    pass


def get_available_from_port_range(from_port, to_port):
    """Returns available local port number.
    """
    r = range(from_port, to_port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for port in r:
        try:
            if sock.connect_ex(('localhost', port)) != 0:
                return port
        finally:
            sock.close()

    raise NoAvailablePortError('No available port between {} and {}'.format(
        from_port, to_port))


def is_ci():
    """Returns if current execution is running on CI

    Returns:
        bool: `True` if current executions is on CI
    """
    return os.getenv('CI', 'false') == 'true'
