import socket

def scan_ports(target, ports):
    print(f"\n--- {target} için tarama başlatılıyor ---\n")
    for port in ports:
        # socket.AF_INET: IPv4, socket.SOCK_STREAM: TCP bağlantısı
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) # Taramanın hızlı olması için zaman aşımı
        
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port}: AÇIK")
        s.close()

if __name__ == "__main__":
    target_ip = input("Hedef IP: ")
    # En yaygın kullanılan portları test edelim
    common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 3389]
    scan_ports(target_ip, common_ports)