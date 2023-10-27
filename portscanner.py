import socket
from IPy import IP
def portscan(ipaddress, port):
  try:
    sock=socket.socket()
    sock.settimeout(0.5)
    sock.connect((ipaddress, port))
    print("port " + str(port) + " is open");
  except:
    print("port " + str(port) + " is closed");
ipaddress=input("[+]Enter the target ipaddress or url: ")
a=int(input("[+]Enter the first port to scan: "))
b=int(input("[+]Enter the final port to scan: "))      
for port in range(a, b):
  portscan(ipaddress, port);
    
     
