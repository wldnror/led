led $ ~/led/demo_wrapper.py
mmap error: : Invalid argument
MMapping from base 0xfe000000, offset 0x3000
mmap error: : Invalid argument
MMapping from base 0xfe000000, offset 0x101000
Suggestion: to slightly improve display update, add
	isolcpus=3
at the end of /boot/cmdline.txt and reboot (see README.md)
FYI: not running as root which means we can't properly control timing unless this is a real-time kernel. Expect color degradation. Consider running as root with sudo.
Size: 128x32. Hardware gpio mapping: regular
Press <CTRL-C> to exit and reset LEDs

