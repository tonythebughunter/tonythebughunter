import socket
from IPy import IP
import sys

def portscan(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        print("Port " + str(port) + " is open")
    except socket.timeout:
        pass
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        sys.exit()  # Exit the script
    finally:
        sock.close()

try:
    ipaddress = input("[+] Enter the target IP address or URL: ")
    a = int(input("[+] Enter the first port to scan: "))
    b = int(input("[+] Enter the final port to scan: "))
    print("Scanning " + str(ipaddress))

    for port in range(a, b):
        portscan(ipaddress, port)

except KeyboardInterrupt:
    print("\nScan interrupted by user.")
    sys.exit()  # Exit the script

     
