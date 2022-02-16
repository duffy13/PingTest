
import platform
from click import command
import subprocess


ip = "8.8.8.8"

def ping(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '5', ip]
    return subprocess.call(command)


print(ping(ip))
