import usb

device_caresens_n = usb.core.find(idVendor=0x0403,idProduct=0x6015)
configuration_index = 0
interface_index = 0
interface_alt_setting = 0
endpoint_in_index = 0

caresens_cfg = device_caresens_n[configuration_index]
caresens_interface = caresens_cfg[(interface_index,interface_alt_setting)]
caresens_in_endpoint = caresens_interface[endpoint_in_index]

print
print ("### caresens_cfg ###")
print (caresens_cfg)

print
print ("### caresens_interface ###")
print (caresens_interface)

print
print ("### caresens_in_endpoint ###")
print (caresens_in_endpoint)

device_caresens_n.set_configuration(caresens_cfg)
# device_caresens_n.detach_kernel_driver(interface_index) # explodes on OSX :( Need to use HIDAPI
# device_caresens_n.set_interface_altsetting(caresens_interface) # explodes on OSX :( Need to use HIDAPI
# device_caresens_n.attach_kernel_driver(interface_index)
# print(device_caresens_n.is_kernel_driver_active(interface_index))

# # No go on OSX - HIDAPI next step. Probably using cython-hidapi
# print
# print ("### caresens_in_endpoint READ attempt ###")
# print (device_caresens_n.read(caresens_in_endpoint,64))


def main():
    pass

if __name__ == "__main__":
    main()
