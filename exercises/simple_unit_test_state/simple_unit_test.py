#!/usr/bin/env python3
import random
import socket
import sys
import time

TYPE_UNIT_TEST = 0x812

from scapy.all import *

class UnitTest(Packet):
    name = "UnitTest"
    fields_desc = [ ByteField("test_id", 0),
                    ByteField("test_status", 0),]

bind_layers(Ether, UnitTest, type=0x812)

def get_if():
    ifs=get_if_list()
    iface=None # "h1-eth0"
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print("Cannot find eth0 interface")
        exit(1)
    return iface

def main():

    iface = get_if()

    pkt =  Ether(src=get_if_hwaddr(iface), dst='00:04:00:00:00:00')
    pkt = pkt / UnitTest(test_id=0, test_status=0)
    while True:
        resp = srp1(pkt, iface=iface, timeout=10, verbose=False)
        resp.show2()
        if resp[UnitTest].test_id == 99:
            break
        pkt =  Ether(src=get_if_hwaddr(iface), dst='00:04:00:00:00:00')
        pkt = pkt / UnitTest(test_id=resp[UnitTest].test_id, test_status=1)
        time.sleep(5)
if __name__ == '__main__':
    main()
