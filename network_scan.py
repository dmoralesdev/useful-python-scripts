import nmap

def scan_network(network):
    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments="-sP")
    hosts = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    return hosts

def get_open_ports(host):
    nm = nmap.PortScanner()
    nm.scan(host, arguments="-p-")
    open_ports = [port for port in nm[host]['tcp'].keys() if nm[host]['tcp'][port]['state'] == 'open']
    return open_ports

network = input("Enter the network to scan (e.g. 192.168.0.0/24): ")
hosts = scan_network(network)
print("Discovered hosts:")
for host, state in hosts:
    open_ports = get_open_ports(host)
    print(f"{host} ({state})")
    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports found")
