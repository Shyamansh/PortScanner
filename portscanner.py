import socket
import termcolor

def scan(target, ports):
    print(f"\n Starting scan for {target}")
    for port in range(1,ports):
        scan_port(target,port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f"[+] checked port {port} is open")
        sock.close()

    except:
        print(f"[-] Tried port {port} closed")


target = input("[*] Enter targets to scan: (split them with comma)")
prt_no = int(input("[*] Enter number of ports to be scaned"))

if ',' in target:
    print(termcolor.colored("Scanning multiple targets", 'green'))
    for ip_addr in target.split(','):
        scan(ip_addr.strip(' '),prt_no)

else:
    scan(target, prt_no)