#!/usr/bin/env python3
import random
import socket
import sys

TYPE_UNIT_TEST = 0x812
from scapy.all import *

class UnitTest(Packet):
    name = "UnitTest"
    fields_desc = [ BitField("test_id", 0, 16),
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

    pkt =  Ether(src=get_if_hwaddr(iface), dst='00:00:00:00:00:02')
    pkt = pkt / UnitTest(test_id=0, test_status=0)
    resp = srp1(pkt, iface=iface, verbose=False)
    resp.show2()


if __name__ == '__main__':
    main()