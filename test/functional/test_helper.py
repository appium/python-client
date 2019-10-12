def get_available_port_range(from_range, to_range):
    """Returns available local port number.
    """
    if isinstance(from_range, int) or isinstance(to_range, int):
        raise ValueError('from_range and to_range should be type of int')

    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for port in range(from_range, to_range):
        try:
            if sock.connect_ex(('localhost', port)) != 0:
                return port
        finally:
            sock.close()
