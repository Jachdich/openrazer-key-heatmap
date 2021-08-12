# openrazer-key-heatmap

Just-for-fun program to log every keypress on a keyboard and colour each key accordingly.

## Installation and usage

Replace your `/usr/lib/python3/dist-packages/openrazer_daemon/misc/key_event_management.py` with `key_event_management.py` from this repo. 

This file seems to be in different places, on arch it was `/usr/lib/python3.9/site-packages/openrazer_daemon/misc/key_event_management.py`.

# !!!!IMPORTANT!!!!

It is very VERY VERY important to specify the heatmap location. This is done by editing the very first line of code. **YOU MUST DO THIS OR THE DRIVER WILL CRASH. IT MUST ALSO BE AN ABSOLUTE PATH THAT WILL NOT CHANGE (i.e. NOT a USB drive)**. sorry for the overemphesis.

When you have a sufficient heatmap generated (after a while of usage) you can run the `generate_heatmap.py` to write the heatmap to the keyboard. It is used like this: `python3 generate_heatmap.py /path/to/heatmap.json`. This should make everything go multicoloured. Note that it needs `keyboard.py` in the same directory.

## Note about heatmap

I have defaulted the heatmap generator to ignore buttons like space and backspace. You can change this by editing the `DISALLOWED_KEYS` list inside `heatmap.py`. The behaviour of the heatmap can also be altered by editing the `colour(times)` function to return a custom colour based on the input of `times`. Have a play with that.

## Sarcasm mode

For a bit of fun I added a feature called sarcasm mode. This looks for a file (Specified, again, on the second line of the program. Leave as None to disable) and if its contents are `true`, toggles capslock every keypress.
