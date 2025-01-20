import scapy.all as scapy

class NetworkTrafficAnalyzer:
    def __init__(self, interface):
        """
        Initialize the analyzer with the network interface to monitor.
        :param interface: Network interface to capture packets (e.g., "eth0", "wlan0").
        """
        self.interface = interface

    def monitor_traffic(self, packet_callback, count=0):
        """
        Monitor network traffic and apply a callback function to each packet.
        :param packet_callback: Function to process each captured packet.
        :param count: Number of packets to capture (0 = infinite).
        """
        scapy.sniff(iface=self.interface, prn=packet_callback, count=count)

# Example usage
# def packet_processor(packet):
#     print(packet.summary())

# analyzer = NetworkTrafficAnalyzer("wlan0")
# analyzer.monitor_traffic(packet_processor)
