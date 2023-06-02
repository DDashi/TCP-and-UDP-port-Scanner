TCP and UDP port Scanner 

A TCP and UDP port scanner that scans ports in a given range from a given host or IP address.
In the case of a found port, the port number is output, the type of protocol on which it is running and the service on which it is running on this port.
Works in multithreaded mode. 

Usage

main.py [-h] [-t] [-u] [-p PORTS [PORTS ...]] ip

Port Scan

positional arguments:
  ip                    TCP scan

optional arguments:
  -h, --help            show this help message and exit
  -t                    TCP scan
  -u                    UDP scan
  -p PORTS [PORTS ...], --ports PORTS [PORTS ...]
                        Ports to scan

Usage example: py main.py localhost -t -u -p 100 1000

Files
The repository contains the following files:

 - `main.py` : Contains code to scan ports.
 - `TCPServer.py` : Contains for startup TCP server on port 50000.
 - `UDPServer.py` : Contains for startup TCP server on port 50001.

This code was written by Емашова Анастасия КН-202.
