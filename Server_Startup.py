import time
from pterodactyl import call_api,call_listapi,parse_data,get_data
from secretinfo import api_key,api_url,re_time

servername=""
servername2=""
x=8

server = call_listapi("GET",api_url,api_key,None)

server = server.text

values = server.split(",")

servername = get_data(values,"identifier")
servername = servername.split(''"identifier"'')
servername = parse_data(servername,":","")
servername = parse_data(servername,'"',"")
servername = parse_data(servername,",,,,",",")
servername = parse_data(servername,",","")

for value in servername:
  servername2 = servername2 + value

res=[servername2[y-x:y] for y in range(x, len(servername2)+x,x)]

for value in res:
  call_api("POST","/power",'{"signal": "start"}',api_key,f"{api_url}servers/{value}")
  time.sleep(re_time)
  print(value)