from pyicloud import PyiCloudService
import sys
import time
import math
from phue import Bridge
import psutil
from datetime import datetime

def startup():
    api = PyiCloudService('devrana925@gmail.com', 'Mango321!')
    if api.requires_2fa:
        print("Two-factor authentication required.")
        code = input("Enter the code you received of one of your approved devices: ")
        result = api.validate_2fa_code(code)
        print("Code validation result: %s" % result)

        if not result:
            print("Failed to verify security code")
            sys.exit(1)

        if not api.is_trusted_session:
            print("Session is not trusted. Requesting trust...")
            result = api.trust_session()
            print("Session trust result %s" % result)

            if not result:
                print("Failed to request trust. You will likely be prompted for the code again in the coming weeks")
    elif api.requires_2sa:
        import click
        print("Two-step authentication required. Your trusted devices are:")

        devices = api.trusted_devices
        for i, device in enumerate(devices):
            print("  %s: %s" % (i, device.get('deviceName',
                "SMS to %s" % device.get('phoneNumber'))))

        device = click.prompt('Which device would you like to use?', default=0)
        device = devices[device]
        if not api.send_verification_code(device):
            print("Failed to send verification code")
            sys.exit(1)

        code = click.prompt('Please enter validation code')
        if not api.validate_verification_code(device, code):
            print("Failed to verify verification code")
            sys.exit(1)
    return api

def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371*1000 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

def lights():
    b = Bridge('192.168.1.167')

    b.connect()
    b.get_api()
    #print(b.get_api())
    #print(b.get_api().keys())
    #print(b.get_api()['lights'])
    #print(b.get_api()['lights']['3'])
    #print(b.get_api()['lights']['4'])
    #print(b.get_api()['lights']['11'])
    print(b.get_group())
    light = b.get_light_objects('id')
    print(light)
    #light[3].brightness = 254
    light[3].on = True
    light[3].hue = 51572
    light[3].saturation = 238

    light[4].on = True
    light[4].hue = 45216
    light[4].saturation = 252

    light[11].on = True
    light[11].hue = 51572
    light[11].saturation = 238

def convert(str):
    if str[-2:] == "AM" and str[:2] == "12":
        return "00" + str[2:-2]
    elif str[-2:] == "AM":
        return str[:-2]
    elif str[-2:] == "PM" and str[:2] == "12":
        return str[:-2]
    else:
        return str(int(str[:2]) + 12) + str[2:8]
def main():
    if("ModernWarfare.exe" in (i.name() for i in psutil.process_iter())):
        lights()
    '''
    api = startup()
    ori = [api.devices[1].location()['latitude'], api.devices[1].location()['longitude']]
    for i in range(5):
        print(i)
        lat = api.devices[1].location()['latitude']
        lon = api.devices[1].location()['longitude']
        print('lat: ', lat)
        print('long: ', lon)
        dest = [api.devices[1].location()['latitude'], api.devices[1].location()['longitude']]
        print("distance: ", distance(ori, dest))
    '''

'''
from phue import Bridge
import time

b = Bridge('192.168.1.167')

b.connect()
b.get_api()
b.get_light(1, 'on')
'''

if __name__ == "__main__":
    main()