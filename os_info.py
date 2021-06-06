import platform
import sys

info = f'OS\n{platform.uname()}\nPython\n{sys.version}, {platform.architecture()}'
print(info)

with open('os_info.txt', 'w') as ff:
    ff.write(info)
