import requests
import pysftp
import time
from pterodactyl import call_api,remove_all_files
from secretinfo import ssh_hos,ssh_usr,ssh_pwd,ssh_por,api_key,ser_url

call_api("POST", "/command", '{"command": "say The Server is being reset in 1 Minute!"}',api_key,ser_url)

time.sleep(60)

call_api("POST", "/power", '{"signal": "stop"}',api_key,ser_url)

time.sleep(60)

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
with pysftp.Connection(ssh_hos, port=ssh_por, username=ssh_usr, password=ssh_pwd, cnopts=cnopts) as sftp:
    remove_all_files(sftp, ".")

time.sleep(10)

call_api("POST", "/settings/reinstall", {},api_key,ser_url)

time.sleep(30)

call_api("POST", "/files/write?file=eula.txt", "eula=true",api_key,ser_url, None)

time.sleep(10)

call_api("POST", "/power", '{"signal": "start"}',api_key,ser_url)