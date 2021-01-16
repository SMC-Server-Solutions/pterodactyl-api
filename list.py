import requests
import pysftp
import time
from pterodactyl import call_listapi
from secretinfo import api_key, api_url

server = call_listapi("GET",api_url,api_key,None)

server = server.text

values = server.split(",")

for value in values:
    print(value)