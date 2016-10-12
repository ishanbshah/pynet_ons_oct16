from getpass import getpass
from pprint import pprint

from napalm_base import get_network_driver
from my_devices import device_list

def main():
    for device in device_list:
        if "junos" in device["device_type"]: 
            dtype = device.pop("device_type")
            driver = get_network_driver(dtype)
            info = driver(**device)
        else:
            continue

        info.open()
        #print "Facts are:"

        print '\n'

        info.load_merge_candidate(config='set routing-options static route 2.2.2.0/24 next-hop 10.220.88.1')
        
        print "comparing:"
        print info.compare_config()
        
        choice = raw_input("Is this good to commit:")
        if choice == 'y' or choice == 'Y':
            print "committing"
            info.commit_config()
        else:
            info.discard_config()

if __name__ == "__main__":

   # with open("config_file.conf", 'w') as config:
   #     config_file=config.write("set routing-options static route 2.2.2.0/24 next-hop 10.220.88.1")
  #  main(config_file)
        main()
