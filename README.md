# open-gluco-caresens

Having a casual hack at getting data out of CareSens meters (at the moment, only the basic CareSens N).

## Contributing

Feel free to contribute. Follow git-flow if possible, but don't worry too much about sticking to it if you aren't overly familiar with it (short version - call feature branches `feature/your-feature`, bug fix branches `fix/your-fix`, open Pull Requests against `develop`).

## Requirements
 - `pyusb` - https://github.com/walac/pyusb
   - the `pyusb` lib requires either `libusb` (0.1 or 1.0) or `OpenUSB`
 - The USB cable for the CareSens N

### Requirements on Mac OS X
Installing with `homebrew` and `pip`:
```
$ brew install libusb
# pre flag required to install pre-release as pyusb hasn't flagged any releases
# as non-beta - so this will install the latest 1.0 beta release (as at 2015-09-21 anyway!)
$ sudo pip install pyusb --pre 
```

## PyUSB Dump - CareSens N

```
DEVICE ID 0403:6015 on Bus 020 Address 018 =================
 bLength                :   0x12 (18 bytes)
 bDescriptorType        :    0x1 Device
 bcdUSB                 :  0x200 USB 2.0
 bDeviceClass           :    0x0 Specified at interface
 bDeviceSubClass        :    0x0
 bDeviceProtocol        :    0x0
 bMaxPacketSize0        :    0x8 (8 bytes)
 idVendor               : 0x0403
 idProduct              : 0x6015
 bcdDevice              : 0x1000 Device 16.0
 iManufacturer          :    0x1 FTDI
 iProduct               :    0x2 FT230X Basic UART
 iSerialNumber          :    0x3 DA01CMA0
 bNumConfigurations     :    0x1
  CONFIGURATION 1: 90 mA ===================================
   bLength              :    0x9 (9 bytes)
   bDescriptorType      :    0x2 Configuration
   wTotalLength         :   0x20 (32 bytes)
   bNumInterfaces       :    0x1
   bConfigurationValue  :    0x1
   iConfiguration       :    0x0 
   bmAttributes         :   0x80 Bus Powered
   bMaxPower            :   0x2d (90 mA)
    INTERFACE 0: Vendor Specific ===========================
     bLength            :    0x9 (9 bytes)
     bDescriptorType    :    0x4 Interface
     bInterfaceNumber   :    0x0
     bAlternateSetting  :    0x0
     bNumEndpoints      :    0x2
     bInterfaceClass    :   0xff Vendor Specific
     bInterfaceSubClass :   0xff
     bInterfaceProtocol :   0xff
     iInterface         :    0x2 FT230X Basic UART
      ENDPOINT 0x81: Bulk IN ===============================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :   0x81 IN
       bmAttributes     :    0x2 Bulk
       wMaxPacketSize   :   0x40 (64 bytes)
       bInterval        :    0x0
      ENDPOINT 0x2: Bulk OUT ===============================
       bLength          :    0x7 (7 bytes)
       bDescriptorType  :    0x5 Endpoint
       bEndpointAddress :    0x2 OUT
       bmAttributes     :    0x2 Bulk
       wMaxPacketSize   :   0x40 (64 bytes)
       bInterval        :    0x0
```

## License
Copyright (c) 2015 James Hill <me@jameshill.io>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
