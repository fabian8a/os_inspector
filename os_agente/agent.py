import os
import socket
import requests
import json
import platform
import psutil
from datetime import datetime

def get_system_info():
    info = {}
    info['cpu'] = platform.processor()
    info['os_username'] = os.getlogin()
    info['os_name'] = platform.system()
    info['server_ip'] = socket.gethostbyname(socket.gethostname())
    info['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    info['os_version'] = platform.version()
    return info


def send_data_to_api(data):
    api_ip = os.getenv('API_IP')
    api_port = os.getenv('API_PORT')
    api_url = 'http://'+api_ip+ ':'+api_port+'/report'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_url, data=json.dumps(data), headers=headers)
    return response.status_code

if __name__ == '__main__':
    system_info = get_system_info()
    http_code = send_data_to_api(system_info)
    if http_code == 200:
        print('success')
    else:
        print('error')
