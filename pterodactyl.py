import requests
import pysftp
import json

def call_api(method, endpoint, data, api_key, fqdn, content_type="application/json"):
    return requests.request(
        method, f"{fqdn}{endpoint}", data=data,
        headers={
            "Authorization": api_key,
            "Accept": "application/json",
            "Content-Type": content_type
        }
    )

def call_listapi(method, endpoint, api_key, content_type="application/json"):
    return requests.request(
        method, f"{endpoint}", data={},
        headers={
            "Authorization": api_key,
            "Accept": "application/json",
            "Content-Type": content_type
        }
    )

def remove_all_files(sftp, dir):
    for file in sftp.listdir(dir):
        fullpath = f"{dir}/{file}"
        if sftp.isdir(fullpath):
            remove_all_files(sftp, fullpath)
            sftp.rmdir(fullpath)
        else:
            sftp.remove(fullpath)

def parse_data(input,variable,separator):
  output = ""
  for value in input:
    output = output + separator + value
  return output.split(variable)

def get_data(input,variable):
    servername = ""
    for value in input:
        num = (value.find(variable,0))
        if num == 1:
            servername = servername + value
    return servername

def api_mysql(api_key,ser_url):
    data = json.loads(call_api("GET", "/databases?include=password","",api_key,ser_url).text)
    attr = data['data'][0]['attributes']
    return (attr['name'],
            attr['host']['address'],
            attr['host']['port'],
            attr['username'],
            attr['relationships']['password']['attributes']['password'])