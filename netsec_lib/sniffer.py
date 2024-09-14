# sniffer.py

from scapy.all import sniff

def capture_traffic(interface, packet_count):
    """
    Fonction pour capturer le trafic réseau en temps réel.
    
    :param interface: Interface réseau à utiliser pour capturer le trafic.
    :param packet_count: Nombre de paquets à capturer avant de s'arrêter.
    """
    def process_packet(packet):
        print(packet.summary())  # Affiche un résumé du paquet capturé
    
    # Capture des paquets sur l'interface spécifiée
    print(f"Sniffing sur {interface}...")
    sniff(iface=interface, prn=process_packet, count=packet_count)

if __name__ == "__main__":
    # Exemple de capture de 10 paquets sur l'interface "eth0"
    capture_traffic("eth0", 10)
