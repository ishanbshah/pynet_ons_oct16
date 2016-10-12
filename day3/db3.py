import django
from net_system.models import NetworkDevice, Credentials

def main():
    django.setup()
    ip_addr1 = raw_input("Enter ip address:")
    ip_addr2 = raw_input("Enter ip address:") 

    test_device1 = NetworkDevice(device_name = 'test1', device_type = 'A10', ip_address = ip_addr1, port = '22')
    test_device1.save()

    test_device2 = NetworkDevice.objects.get_or_create(device_name = 'test2', device_type = 'Netscaler', ip_address = ip_addr2, port = '22')
    
    net_address = NetworkDevice.objects.all()
    for devices in net_address:
        print devices, devices.device_type

if __name__ == "__main__":
    main()
