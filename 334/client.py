from contextlib import suppress
from hashlib import sha256
from socket import socket, AF_INET, SOCK_STREAM
from typing import Tuple


def socket_client(address: Tuple[str, int], server_message_length: int):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(address)
        while True:
            rdata = s.recv(server_message_length)
            if not rdata:
                break
            return_message = sha256(rdata).digest()
            s.sendall(return_message)
