# -*- coding: utf-8 -*-
import socket
import mux_adc

HOST = '192.168.0.6'
PORT = 8000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.sendall('Hello'.encode())

data = client_socket.recv(1024)
print('Received', repr(data.decode()))

client_socket.close()