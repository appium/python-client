def get_available_port_range(from_range, to_range):
    """Returns available local port number.
    """
    if not isinstance(from_range, int) or not isinstance(to_range, int):
        raise ValueError('"{}" and "{}" should be type of int'.format(from_range, to_range))

    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for port in range(from_range, to_range):
        try:
            if sock.connect_ex(('localhost', port)) != 0:
                return port
        finally:
            sock.close()
