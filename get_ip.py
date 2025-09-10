#!/usr/bin/env python3
"""
Script simple para obtener la IP local
"""

import socket

def get_local_ip():
    """Obtiene la IP local de la PC."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except:
        return '127.0.0.1'

if __name__ == "__main__":
    print(get_local_ip())
