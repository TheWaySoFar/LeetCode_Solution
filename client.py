#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024).decode('utf-8'))
for name in [b'Michael', b'Tracy', b'Sarah']:
    s.send(name)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
