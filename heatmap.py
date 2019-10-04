import colorsys
import random
import json, math, sys

if len(sys.argv) < 2:
    print("Error: heatmap file needed")
    sys.exit(1

from openrazer.client import DeviceManager
from openrazer.client import constants as razer_constants

from keyboard import layouts

try:
    with open(sys.argv[1], "r") as f:
        data = json.loads(f.read())
except:
    print("Heatmap file unaccessable!")
    sys.exit(1)
        
MAX = -1

DISALLOWED_KEYS = ["space", "backspace", "leftarrow", "rightarrow", "downarrow", "uparrow"] #common keys that would mess up the other keys

for key in data:
    if data[key] > MAX and key.lower() not in DISALLOWED_KEYS:
        MAX = data[key]

# Create a DeviceManager. This is used to get specific devices
device_manager = DeviceManager()

devices = device_manager.devices
for device in devices:
    if not device.fx.advanced:
        devices.remove(device)


# Disable daemon effect syncing.
# Without this, the daemon will try to set the lighting effect to every device.
device_manager.sync_effects = False

def hsv2rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b


def getKey(row, col):
    try:
        return layouts["reference"][row][col]
    except:
        return None

def colour(times):
    times_normal = times / MAX * 360
    if times_normal > MAX:
        times_normal = MAX - 0.1
    return hsv2rgb(times_normal, 1, 1)


for device in devices:
    rows, cols = device.fx.advanced.rows, device.fx.advanced.cols

    for row in range(rows):
        for col in range(cols):
            key = getKey(row, col)
            times = data.get(key.upper(), 0)
            device.fx.advanced.matrix[row, col] = colour(times)
    device.fx.advanced.draw()
