# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 10:39:24 2020

@author: Pranav Devarinti
"""

import socket

def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'UTF-8'))
        response = str(sock.recv(1024), 'UTF-8')
        print("Received: {}".format(response))
        sock.sendall(bytes("disconnect", 'UTF-8'))
client("2.tcp.ngrok.io",11651,"ABC")