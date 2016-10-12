from getpass import getpass
from pprint import pprint

from napalm_base import get_network_driver
from my_devices import device_list

def main():
    for device in device_list:
        dtype = device.pop("device_type")
        driver = get_network_driver(dtype)
        info = driver(**device)

        info.open()
        print "Facts are:"
        facts = info.get_facts()
        print facts 

        print '\n'

        print "{hostname}: and {model}:".format(**facts)

if __name__ == "__main__":
    main()        
