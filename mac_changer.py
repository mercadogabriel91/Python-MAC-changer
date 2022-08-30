#!/usr/bin/env python

# MODULES IMPORTS
import subprocess
import optparse
import re


# Get arguments and set options
def getArguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface to change it's MAC address")
    parser.add_option("-m", "--mac", dest="new_mac",
                      help="new MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error(
            "[-] Please specify an interfeace, use --help for more info.")
    elif not options.new_mac:
        parser.error(
            "[-] Please specify a new mac address, use --help for more info.")
    return options


# Change MAC address function
def change_mac(interface, new_mac):
    print("[+] changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


# Get current mac address for the interface
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_addr_result = re.search(
        r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_addr_result:
        return mac_addr_result.group(0)
    else:
        print("[-] Could not read the MAC address")


options = getArguments()
current_mac = get_current_mac(options.interface)
print("Current MAC: " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)

if current_mac == get_current_mac(options.interface):
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[+] MAC address did NOT get changed")
