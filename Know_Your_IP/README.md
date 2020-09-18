# Know Your IP

> The IPv4 address is a 32-bit number that uniquely identifies a network interface on a machine. An IPv4 address is typically written in decimal digits, formatted as four 8-bit fields that are separated by periods. Each 8-bit field represents a byte of the IPv4 address.

> Each IPv4 address contains two primary parts: the network prefix and the host number. All hosts within a single network share the same network address. Each host also has an address that uniquely identifies it. Seperate IP classes are used for different types of networks.


*__IPv4 address classes__* 

> Class A IP addresses, where the 1st bit is 0, encompass the range of 0.0.0.0 to 127.255.255.255. This class is for large networks and has 8 bits for network and 24 bits for hosts.

> Class B IP addresses, where the 1st two bits are 10, are in the range of 128.0.0.0 to 191.255.255.255. This class is for medium networks and has 16 bits for network and 16 bits for hosts.

> Class C IP addresses, where the 1st three bits are 110, are in the range of 192.0.0.0 to 223.255.255.255. This class is for smaller networks and has 24 bits for network and 8 bits for hosts.

> Class D or multicast IP addresses, where the 1st four bits are 1110 are in the range of 254.0.0.0 to 239.255.255.255.

> Class E or experimental IP addresses, where the 1st four bits are 11110, are in the range of 192.0.0.0 to 254.255.255.255.

*__Subnet Mask__*

> A subnet mask is a 32- or 128-bit number that segments an existing IP address in a TCP/IP network. It is used by the TCP/IP protocol to determine whether a host is on the local subnet or on a remote network.

*__Network__* 

> This part specifies the unique number address to your network. It also identifies the class of network assigned. In the network part takes up two bytes of the IP address.

*__Host ID__* 

> This is the part of the IP address that you assign to each host. It uniquely identifies this machine on your network. Note that for each host on your network, the network part of the address will be the same, but the host part must be different.