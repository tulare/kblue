# -*- encoding: utf-8 -*-

import dbus
import subprocess
from xml.etree import ElementTree

from .nodes.const import *

# --- ObjectManager -----------------------------------------------------

def get_object_manager() :
    bus = dbus.SystemBus()
    manager = dbus.Interface(
        bus.get_object("org.bluez", "/"),
        DBUS_OM_INTERFACE
    )
    return manager

def get_managed_objects():
    manager = get_object_manager()
    return manager.GetManagedObjects()

def find_objects(interface_name) :
    return find_objects_with_interface(
        get_managed_objects(),
        interface_name
    )

def find_objects_with_interface(objects, interface_name) :
    interfaces = []
    bus = dbus.SystemBus()
    path_prefix = ""
    for path, ifaces in objects.items() :
        interface = ifaces.get(interface_name)
        if interface is None :
            continue
        if path.startswith(path_prefix) :
            obj = bus.get_object(SERVICE_NAME, path)
            interfaces.append(dbus.Interface(obj, interface_name))
    return interfaces

def find_objects_match(interface_mask='') :
    interfaces = []
    bus = dbus.SystemBus()
    path_prefix = ""
    for path, ifaces in sorted(get_managed_objects().items()) :
        for iface in ifaces :
            if  interface_mask in str(iface) :
                obj = bus.get_object(SERVICE_NAME, path)
                interfaces.append(dbus.Interface(obj, iface))
    return interfaces

# --- Adapter1 ----------------------------------------------------------

def find_adapter(pattern=None):
    return find_adapter_in_objects(get_managed_objects(), pattern)


def find_adapter_in_objects(objects, pattern=None):
    bus = dbus.SystemBus()
    for path, ifaces in objects.items():
        adapter = ifaces.get(ADAPTER_INTERFACE)
        if adapter is None:
            continue
        if not pattern or pattern == adapter["Address"] or \
                            path.endswith(pattern):
            obj = bus.get_object(SERVICE_NAME, path)
            return dbus.Interface(obj, ADAPTER_INTERFACE)
    raise Exception("Bluetooth adapter not found")

# --- Device1 ----------------------------------------------------------

def find_devices(adapter_pattern=None) :
    return find_objects_with_interface(
        get_managed_objects(),
        DEVICE_INTERFACE
    )

def find_devices_with_uuid(uuid, adapter_pattern=None) :
    return [
        dev
        for dev in find_devices(adapter_pattern)
        if str(uuid) in get_property(dev, 'UUIDs')
    ]

def find_device(device_address, adapter_pattern=None) :
    return find_device_in_objects(
        get_managed_objects(),
        search_value=device_address, search_field='Address',
        adapter_pattern=adapter_pattern
    )


def find_device_byname(device_name, adapter_pattern=None) :
    return find_device_in_objects(
        get_managed_objects(),
        search_value=device_name, search_field='Name',
        adapter_pattern=adapter_pattern
    )

def find_device_in_objects(objects, search_value, search_field='Address', adapter_pattern=None):
    bus = dbus.SystemBus()
    path_prefix = ""
    if adapter_pattern:
        adapter = find_adapter_in_objects(objects, adapter_pattern)
        path_prefix = adapter.object_path
    for path, ifaces in objects.items():
        device = ifaces.get(DEVICE_INTERFACE)
        if device is None:
            continue
        if (device[search_field] == search_value and
                        path.startswith(path_prefix)):
            obj = bus.get_object(SERVICE_NAME, path)
            return dbus.Interface(obj, DEVICE_INTERFACE)

    raise Exception("Bluetooth device not found")

# --- Properties -----------------------------------------------------

def list_properties(obj) :
    xml = introspect(obj)
    tree = ElementTree.fromstring(xml)
    properties = {}
    for intf in tree.findall('interface') :
        if intf.attrib.get('name') == obj.dbus_interface :
            for prop in intf.findall('property') :
                properties[prop.attrib.get('name')] = (
                    prop.attrib.get('type'),
                    prop.attrib.get('access')
                )            
    return properties

def get_property(obj, prop_name) :
    properties = dbus.Interface(
        obj,
        dbus_interface='org.freedesktop.DBus.Properties'
    )    
    return properties.Get(obj.dbus_interface, prop_name)
    

def set_property(obj, prop_name, prop_value) :
    properties = dbus.Interface(
        obj,
        dbus_interface='org.freedesktop.DBus.Properties'
    )    
    return properties.Set(obj.dbus_interface, prop_name, prop_value)
    
def get_properties(obj) :
    properties = dbus.Interface(
        obj,
        dbus_interface='org.freedesktop.DBus.Properties'
    )    
    return properties.GetAll(obj.dbus_interface)

# --- Introspectable -----------------------------------------------------

def introspect(obj) :
    introspectable = dbus.Interface(
        obj,
        dbus_interface='org.freedesktop.DBus.Introspectable'
    )
    return introspectable.Introspect()

def introspect_dump(dest, path, recurse=False, only_properties=False) :
    options = []
    if recurse :
        options.append('--recurse')
    if only_properties :
        options.append('--only-properties')
    command = [
        'gdbus', 'introspect', '--system',
        '--dest', dest,
        '--object-path', path,
        *options
    ]
    output = subprocess.check_output(command, universal_newlines=True)
    print(output)

# --- Interfaces --------------------------------------------------------

def list_interfaces(obj) :
    xml = introspect(obj)
    tree = ElementTree.fromstring(xml)
    interfaces = [
        intf.attrib['name']
        for intf in tree.findall('interface')
    ]
    return interfaces

def find_interface(interface_name, with_obj=None) :
    return find_interface_in_objects(
        get_managed_objects(),
        interface_name,
        with_obj=with_obj
    )

def find_interface_in_objects(objects, interface_name, with_obj=None):
    bus = dbus.SystemBus()
    path_prefix = ""
    for path, ifaces in objects.items():
        interface = ifaces.get(interface_name)
        if interface is None:
            continue
        if ((with_obj is None and path.startswith(path_prefix)) or
            (with_obj and path == with_obj.object_path)) :
            obj = bus.get_object(SERVICE_NAME, path)
            return dbus.Interface(obj, interface_name)
    raise Exception("Bluetooth interface not found")

# --- Nodes ------------------------------------------------------------

def list_nodes(obj) :
    xml = introspect(obj)
    tree = ElementTree.fromstring(xml)
    nodes = [
        node.attrib['name']
        for node in tree.findall('node')
    ]
    return nodes

# --- Methods ----------------------------------------------------------

def list_methods(obj) :
    xml = introspect(obj)
    tree = ElementTree.fromstring(xml)
    methods = dict()
    for intf in tree.findall('interface') :
        if intf.attrib.get('name') == obj.dbus_interface :
            for meth in intf.findall('method') :
                args = [ arg.attrib for arg in meth.findall('arg') ]
                methods[meth.attrib.get('name')] = args
##    for meth in tree.xpath('interface[@name="{}"]/method'.format(obj.dbus_interface)) :
##        args = [ e.attrib for e in meth.xpath('arg') ]
##        methods[meth.attrib.get('name')] = args
    return methods

# --- Signals ---------------------------------------------------------

def list_signals(obj) :
    xml = introspect(obj)
    tree = ElementTree.fromstring(xml)
    signals = []
    for intf in tree.findall('interface') :
        for signal in intf.findall('signal') :
            signals.append(intf.attrib.get('name') + '.' + signal.attrib.get('name')) 
    # signals = tree.xpath('interface[@name="{}"]/signal/@name'.format(obj.dbus_interface))
    return signals

