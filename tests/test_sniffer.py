# test_sniffer.py

import unittest
from netsec_lib.sniffer import capture_traffic

class TestSniffer(unittest.TestCase):
    def test_sniffer_interface(self):
        # Test simple pour vérifier la capture de paquets sur une interface.
        try:
            capture_traffic("lo", 5)  # Loopback interface, capture de 5 paquets
        except Exception as e:
            self.fail(f"Sniffer échoué avec erreur: {e}")

if __name__ == '__main__':
    unittest.main()
