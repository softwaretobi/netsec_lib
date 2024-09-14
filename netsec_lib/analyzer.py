# analyzer.py

from scapy.all import IP, TCP, UDP

def analyze_packet(packet):
    """
    Analyse le contenu d'un paquet.
    
    :param packet: Le paquet capturé par scapy.
    :return: Détails analysés du paquet.
    """
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"Paquet IP: {ip_src} -> {ip_dst}")
        
        if TCP in packet:
            print(f"Protocole: TCP, Port source: {packet[TCP].sport}, Port destination: {packet[TCP].dport}")
        elif UDP in packet:
            print(f"Protocole: UDP, Port source: {packet[UDP].sport}, Port destination: {packet[UDP].dport}")
    else:
        print("Paquet non-IP capturé")

