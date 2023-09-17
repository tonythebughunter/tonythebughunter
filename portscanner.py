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
ipaddress=input("[+]Enter the target ipaddress: ")
for port in range(70, 100):
  portscan(ipaddress, port);
    
     
