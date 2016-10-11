from netmiko import ConnectHandler
from Switches import cisco
from Switches import arista

def file(f, run):
    with open(f, "w") as filename:
        filename.write(run)

def main():
    netconnect1 = ConnectHandler(**cisco.dic)
    netconnect2 = ConnectHandler(**arista.dict)

    print "Current prompt for Cisco:" + netconnect1.find_prompt()
    print "Current prompt for Arista:" + netconnect1.find_prompt()


    output1 = netconnect1.send_command("show version")
    output2 = netconnect2.send_command("show version")
    
    print output1
    print "\n"
    print output2

    f1 = "run_command_cisco.txt"
    output3 = netconnect1.send_command("show run")
    file(f1, output3)
    f2 = "run_command_arista.txt"
    output4 = netconnect2.send_command("show run")
    file(f2, output4)

if __name__ == "__main__":
    main()
    
