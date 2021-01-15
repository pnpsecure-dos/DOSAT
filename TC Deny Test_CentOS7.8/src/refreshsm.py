#!/usr/bin/python

import socket as skt

usock = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
usock.sendto('.'.encode(), ('192.168.105.181',21114))
