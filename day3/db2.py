import django
from net_system.models import NetworkDevice, Credentials

def main():
    django.setup()
    net_devices = NetworkDevice.objects.all()
    for devices in net_devices:
        if "cisco" in devices.device_type:
            devices.vendor = "Cisco"
        elif "arista" in devices.device_type:
            devices.vendor = "Arista"
        else:
            devices.vendor = "Juniper"
        devices.save()
    for devices in net_devices:
        print devices,'\t',devices.vendor

if __name__ =="__main__":
    main()
