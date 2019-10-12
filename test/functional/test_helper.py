def get_available_port(in_range):
    """Returns available local port number.
    """
    range(8102, 8200)
    if isinstance(in_range, range):
        raise ValueError('{} should be range'.format(in_range))

    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for port in in_range:
        if sock.connect_ex(('localhost', port)) != 0:
            sock.close()
            return port
        sock.close()
