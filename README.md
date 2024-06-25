# Overview

This repository contains a Python program that reads in a packet capture (PCAP) file, and prints information about each packet.

## Requirements
* Python 3

## Files
* pcaptools.py
* sniffed.pcap (11 MB)

# Instructions

1. Clone repository: `git clone https://github.com/mchow01/scapy-ml-wtw`
2. `cd scapy-ml-wtw`
3. `python3 -m venv env` # this will create a Python virtual environment
4. `source env/bin/activate` # activate the Python virtual environment
5. `pip3 install scapy` # install Scapy
6. `python3 pcaptools.py` # output should be a number of lines (5997 to be exact), and ends with "There were 5997 packets in sniffed.pcap"
7. `deactivate` # this will exit the Python virtual environment