# Light-Automation
Goal is to automate the lights in my room to do various things.

- Use phue API to connect to Philips Hue lights and change the scenes (https://github.com/studioimaginaire/phue)
- Use psutil to check which applications are running on my Windows PC (https://pypi.org/project/psutil/)
- Use PyiCloudService to find the location of my phone (https://pypi.org/project/pyicloud/)

## Step 1
Use psutil to find which applications are being used. So far, will have to manually input the string of the application that you want the lights to change to. For my application, this checks if "ModernWarefare.exe" is running and will change the lights to a gaming mode.

```python
if("ModernWarefare.exe" in (i.name() for i psutil.process_iter())):
  lights()
```

## Step 2
Use time to find what time it is and whether it is past a certain time so that the lights go from gaming mode to sleep mode, gaming mode to regular lights, or automatically go to sleep mode after a certain time.

Sudo Code:
```python
if game_is_played():
  if time > 00:00:00 and time < 05:00:00:
    sleep_mode()
  else:
    regular_mode()
else:
  regular_mode()
```

## Step 3
Use PyiCloudService to find latitude and longitude of my phones location to see how far away it is from the PC. Ideally, if I am farther than 5 meters for more than 2 minutes, the lights will turn off.

Difficulties:
- Accuracy of the distance travelled over time
