from netmiko import ConnectHandler
from Switches import arista


def main():
    netconnect1 = ConnectHandler(**arista.dict)
    
    cmd = ['vlan 901', 'name script_vlan']
    output = netconnect1.send_config_set(cmd)
    print output
    print "\n"
    filename = "vlan_file.txt"
    with open(filename, "w") as f:
         f.write("vlan 900 \n name vlan_file")
    
    netconnect1.send_config_from_file(filename)


if __name__ == "__main__":
    main()
