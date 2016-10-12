from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable

def main():
    password = getpass()
    device = Device(host = '184.105.247.76', user = 'pyclass', password = password)
    
    device.open()
    eth = EthPortTable(device)
    eth.get()
    
    for interface,v in eth.items():
        if interface == "fe-0/0/7":
            print "interface {}".format(interface)
            for field, value in v:
                if 'bytes' in field:
                    print "{} equals {}".format(field, value)

if __name__ == "__main__":
    main()
