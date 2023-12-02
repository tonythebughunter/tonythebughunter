import socket
def portscan(ipaddress, port):
  try:
    sock=socket.socket()
    sock.settimeout(0.5)
    sock.connect((ipaddress, port))
    print("port " + str(port) + " is open");
  except:
    n=0;
ipaddress=input("[+]Enter the target ipaddress or url: ")
a=int(input("[+]Enter the first port to scan: "))
b=int(input("[+]Enter the final port to scan: "))
print("Scanning " + ipaddress + " ...")
for port in range(a, b+1):
  portscan(ipaddress, port);
    
     
