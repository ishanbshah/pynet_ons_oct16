from getpass import getpass
from pprint import pprint
from jinja2 import Template

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.op.routes import RouteTable

XML_TEMPLATE = """
<configuration>
            <routing-options>
                <static>
                    <route>
                        <name>{{ prefix }}</name>
                        <next-hop>{{ next_hop }}</next-hop>
                    </route>
                </static>
            </routing-options>
</configuration>
"""

def display_static_routes(device):
    route = RouteTable(device)
    route.get()
    
    print "Current routes:"
    for line in route.get():
        pprint(line)

def gen_template(dic):
    xml_route = Template(XML_TEMPLATE)
    return str(xml_route.render(**dic))

def main():
    password = getpass()
    device = Device(host = '184.105.247.76', user = 'pyclass', password = password)
    
    rdict = {'prefix':'1.1.1.0/24', 'next_hop':'10.220.88.1'}
    new_route = gen_template(rdict)
    
    device.open()
    display_static_routes(device)
    config = Config(device)
    config.lock()

    config.load(new_route, format = 'xml', merge = True)
    print '\n'
    print config.diff()
    
    config.commit()
    display_static_routes(device)
    
    config.unlock()

if __name__ == "__main__":
    main() 
