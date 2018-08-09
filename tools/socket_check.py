#!/usr/local/bin/python

import socket

def check_port(address,port):
    s = socket.socket()

    try:
        s.connect((address, port))
        return True
    except socket.error,e:
        print("%s:%s failed"%(address,port))
        return False

def get_address(filename):
    address = []
    port = []
    with open(filename) as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        line = line.split(' ') if len(line.split(' '))==2 else line.split(':')
        address.append(line[0])
        port.append(line[1])
    return address, port


if __name__ == '__main__':

    f = 'ip.txt'
    addresses, ports = get_address(f)
    for (address, port) in zip(addresses, ports):
        check_port(address,int(port))
