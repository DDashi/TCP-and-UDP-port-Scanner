import socket
import threading
import argparse


def scan_tcp_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"TCP Port {port} is open")
            # Определение протокола
            service = socket.getservbyport(port, 'tcp')
            print(f"Service: {service}")
        sock.close()
    except socket.error:
        pass


def scan_udp_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)
        sock.sendto(b"Probe", (host, port))
        data, addr = sock.recvfrom(1024)
        print(f"UDP Port {port} is open")
        # Определение протокола
        service = socket.getservbyport(port, 'udp')
        print(f"Service: {service}")
        sock.close()
    except socket.error:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Port Scan')
    parser.add_argument('ip', type=str, default="localhost", help='TCP scan')
    parser.add_argument('-t', action='store_true', help='TCP scan')
    parser.add_argument('-u', action='store_true', help='UDP scan')
    parser.add_argument('-p', '--ports', nargs='+', type=int, default=[1, 55000], help='Ports to scan')
    args = parser.parse_args()
    host = args.ip
    start_port = args.ports[0]
    end_port = args.ports[1]

    print(f"Scanning ports on {host}...")
    for port in range(start_port, end_port + 1):
        if args.t:
            threading.Thread(target=scan_tcp_port, args=(host, port)).start()
        if args.u:
            threading.Thread(target=scan_udp_port, args=(host, port)).start()
    print(f"Scan finish")
