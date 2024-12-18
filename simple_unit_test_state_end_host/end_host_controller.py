#!/usr/bin/env python3
import os
import sys

from scapy.all import *
ifaces = [i for i in os.listdir('/sys/class/net/') if 'eth0' in i]
iface = ifaces[0]
counter = {}
counter[0] = 0
MAX_UNIT_TESTS = 100

class UnitTest(Packet):
    name = "UnitTest"
    fields_desc = [ BitField("test_id", 0, 16),
                    ByteField("test_status", 0),]

bind_layers(Ether, UnitTest, type=0x812)

def get_if():
    ifs=get_if_list()
    iface=None
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print("Cannot find eth0 interface")
        exit(1)
    return iface

def handle_pkt(pkt):
#    hexdump(pkt)
    if UnitTest in pkt and pkt[Ether].src != "08:00:00:00:05:55":
        dst = pkt[Ether].src
        tmp_count = counter[0]
        tmp_count += 1
        counter[0] = tmp_count
        if tmp_count > 100:
            target_test_id = 999
        else:
            target_test_id = tmp_count - 1
        pkt =  Ether(src=get_if_hwaddr(iface), dst=dst)
        pkt = pkt / UnitTest(test_id=target_test_id, test_status=0)
        pkt.show2()
        sys.stdout.flush()
        sendp(pkt, iface=iface, verbose=False)

def main():
    print("sniffing on %s" % iface)
    sys.stdout.flush()
    print(get_if_hwaddr(iface))

    sniff(iface = iface,
          prn = lambda x: handle_pkt(x))

if __name__ == '__main__':
    main()
