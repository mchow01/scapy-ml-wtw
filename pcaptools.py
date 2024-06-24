#!/usr/bin/python3

from scapy.all import *

packets = sniff(offline='sniffed.pcap')
count = 0
for packet in packets:
    print(packet)
    count += 1
print(f"There were {count} packets in sniffed.pcap")