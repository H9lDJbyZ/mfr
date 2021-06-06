import platform
import sys

info = f'OS {platform.uname()}, Python {sys.version}, {platform.architecture()}'
print(info)

with open('os_info.txt', 'w') as ff:
    ff.write(info)