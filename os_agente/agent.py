import os
import socket
import requests
import json
import platform
import psutil
from datetime import datetime

def get_system_info():
    info = {}
    info['processor'] = platform.processor()
    info['os_name'] = platform.system()
    info['server_ip'] = socket.gethostbyname(socket.gethostname())
    info['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    info['os_version'] = platform.version()
    return info

print(get_system_info())