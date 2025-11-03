from scapy.all import *
interface = 'wlan0'
probeReqs = []

def sniffProves(p):

    if p.haslayer(Dot11ProbeReq):
        netname = p.getlayer(Dot11ProbeReq).info
        if netname not in probeReqs:
            probeReqs.append(netname)
            print('[+] Detected New Probe Request for: ' + netName)

sniff(iface=interface, prn=sniffProves)