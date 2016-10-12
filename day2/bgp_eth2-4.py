import time
from getpass import getpass
from getpass import getuser
from pynxos.device import Device
from pynxos.errors import CLIError

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from pprint import pprint


# Disable untrusted CERT warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def check_errors(result, verbose=False):
    for entry in result:
        if entry is not None:
            if verbose:
                print entry
            else:
                return False
    return True


def main():
    switch_ip = raw_input("Enter switch ip:")
    username = "pyclass"
    password = getpass()
    eth_int = "Ethernet 2/4"
    interface_ip = "10.1.4.1/24"
    peer_ip = "10.1.4.2"
    as_number = "10"
    
    int_conf = ['interface {}'.format(eth_int), 'ip address {}'.format(interface_ip)]

    bgp_conf = ['router bgp {}'.format(as_number), 'neighbor {} remote-as {}'.format(peer_ip, as_number), 'address-family ipv4 unicast']
    nexus = Device(host = switch_ip, username = username, password = password, transport = 'https', port = '8443')
    

    #configuring interface
    result = nexus.config_list(int_conf)
    if check_errors(result) == True:
        print "Interface configured"
    else:
        print "Failed config"

       #show current bgp status

    print "Current bgp status is:"
    cmd = 'show ip bgp summary'
    print nexus.show(cmd, raw_text=True) 
    
    #configuring bgp
    result = nexus.config_list(bgp_conf)
    if check_errors(result) == True:
        print "bgp configured"
    else:
        print "bgp not configured"
    
    time.sleep(5)
    #show bgp
    print "Checking if bgp is established"
    cmd = 'show ip bgp summary'
    print nexus.show(cmd, raw_text=True)
    if "Active" or "Idle" in nexus.show(cmd):
        print "Fail"
    else:
        print "pass"

    print nexus.save()

if __name__ == "__main__":
    main()
