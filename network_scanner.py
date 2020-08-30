#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    request_broadcast_packet = broadcast / arp_request
    return scapy.srp(request_broadcast_packet, timeout=1, verbose=False)[0]


def print_result(answered_list):
    print("IP\t\t\tMAC Address")
    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    for client in client_list:
        print(client["ip"] + "\t\t" + client["mac"])


answer = scan("10.0.2.1/24")
print_result(answer)

