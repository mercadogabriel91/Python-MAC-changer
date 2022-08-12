#!/usr/bin/env python
import subprocess
import optparse


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


def change_mac(interface, new_mac):
    print("[+] changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = getArguments()

change_mac(options.interface, options.new_mac)
