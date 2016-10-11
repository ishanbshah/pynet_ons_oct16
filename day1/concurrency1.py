from netmiko import ConnectHandler
import threading
from my_devices import device_list
from datetime import datetime


def net_connect(device, cmd):
    netconnect = ConnectHandler(**device)
    output = netconnect.send_command(cmd)
    print output
    print "\n"

    
def main():
    start_time = datetime.now()
    for device in device_list:
        if 'juniper' in device['device_type']:
            cmd = 'show config'
        else:
            cmd = 'show run'
        my_thread = threading.Thread(target=net_connect, args=(device, cmd))
        my_thread.start()

    
    main_thread = threading.currentThread()
    for thread in threading.enumerate():
        if thread != main_thread:
            thread.join()    
    end_time = datetime.now()
    print "Time elapsed: {}".format(end_time - start_time)

if __name__ == "__main__":
    main()        
