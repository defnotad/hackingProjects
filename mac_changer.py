#!/usr/bin/env python3

import subprocess
import optparse
import re


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC")
    parser.add_option("-m", "--mac", dest="new_address", help="The address to change it to")
    (options, args) = parser.parse_args()
    if options.interface and options.new_address:
        return options
    else:
        parser.error("Please specify the correct arguments, use --help for more info")


def change_mac(interface, new_address):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_address])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if search_result:
        return search_result.group(0)
    else:
        print("Could not read address")


options = get_args()
change_mac(options.interface, options.new_address)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_address:
    print("Successfully changed MAC address to: " + str(current_mac))
else:
    print("Could not change MAC address")
