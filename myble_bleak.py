# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 14:33:37 2019

@author: hosna
"""
import abc
from typing import List, Union, Iterator
import asyncio
from bleak import discover
import platform
import logging
from bleak import BleakClient
from bleak import _logger as logger
from bleak.uuids import uuidstr_to_str
from bleak.backends.characteristic import BleakGATTCharacteristic
from bleak.backends.descriptor import BleakGATTDescriptor
import nest_asyncio


devices = []
nest_asyncio.apply()
async def scan():
    dev = await discover()
    for i in range(0,len(dev)):
        print("["+str(i)+"]"+str(dev[i]))
        devices.append(dev[i])

from bleak import BleakClient

async def connect(address, loop):
    async with BleakClient(address, loop=loop) as client:
        services = await client.get_services()
        for ser in services:
            print(ser.uuid)

loop = asyncio.get_event_loop()
loop.run_until_complete(scan())
index = input('please select device from 0 to '+str(len(devices))+":")
index = int(index)
loop.run_until_complete(connect(devices[index].address, loop))

async def print_services(mac_addr: str, loop: asyncio.AbstractEventLoop):
    async with BleakClient(mac_addr, loop=loop) as client:
        svcs = await client.get_services()
        print("Services:", svcs)
mac_addr = (
    "34:03:DE:43:6D:D5"
)
loop = asyncio.get_event_loop()
loop.run_until_complete(print_services(mac_addr, loop))


async def run(address, loop, debug=False):
    log = logging.getLogger(__name__)
    if debug:
        import sys
        loop.set_debug(True)
        log.setLevel(logging.DEBUG)
        h = logging.StreamHandler(sys.stdout)
        h.setLevel(logging.DEBUG)
        log.addHandler(h)

    async with BleakClient(address, loop=loop) as client:
        x = await client.is_connected()
        log.info("Connected: {0}".format(x))

        for service in client.services:
            log.info("[Service] {0}: {1}".format(service.uuid, service.description))
            for char in service.characteristics:
                if "read" in char.properties:
                    try:
                        value = bytes(await client.read_gatt_char(char.uuid))
                    except Exception as e:
                        value = str(e).encode()
                else:
                    value = None
                log.info(
                    "\t[Characteristic] {0}: ({1}) | Name: {2}, Value: {3} ".format(
                        char.uuid, ",".join(char.properties), char.description, value
                    )
                )

                for descriptor in char.descriptors:
                    value = await client.read_gatt_descriptor(descriptor.handle)
                    log.info(
                        "\t\t[Descriptor] {0}: (Handle: {1}) | Value: {2} ".format(
                            descriptor.uuid, descriptor.handle, bytes(value)
                        )
                    )

if __name__ == "__main__":
    address = (
        "34:03:DE:43:6D:D5"
    )
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(address, loop, True))
"""
address = "34:03:DE:43:6D:D5"
MODEL_NBR_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

async def run(address, loop):
    async with BleakClient(address, loop=loop) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

loop = asyncio.get_event_loop()
loop.run_until_complete(run(address, loop)) 

async def print_services(mac_addr: str, loop: asyncio.AbstractEventLoop):
    async with BleakClient(mac_addr, loop=loop) as client:
        svcs = await client.get_services()
        print("Services:", svcs)

mac_addr = (

    "24:71:89:cc:09:05"

    if platform.system() != "Darwin"

    else "243E23AE-4A99-406C-B317-18F1BD7B4CBE"

)

loop = asyncio.get_event_loop()
loop.run_until_complete(print_services(mac_addr, loop))


nest_asyncio.apply()
async def run():
    devices = await discover()
    for d in devices:
        print(d)

loop = asyncio.get_event_loop()
loop.run_until_complete(run()) 
"""

