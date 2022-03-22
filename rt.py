import os
import sys
import random
import time
import re
import requests
import user_agent
from user_agent import generate_user_agent

A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"
M = "\033[1;94m"


def baner():
	banera ="""\033[1;92m
	
     888     888 8888888b.       Y88b   d88P 
     888     888 888   Y88b       Y88b d88P  
     888     888 888    888        Y88o88P   
     888     888 888   d88P         Y888P    
     888     888 8888888P"          d888b    
     888     888 888      888888   d88888b   
     Y88b. .d88P 888              d88P Y88b  
      "Y88888P"  888             d88P   Y88b 
                    
\033[1;93m < \033[1;92mTHE SCRIPT INSTA UP  \033[1;93m >  \033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : SIDRA ELEZZ
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : HrHrr
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : TERMUX TOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/SIDRAELEZZ\033[1;91m
  ---------------------------
"""                  
	for sidra in banera.splitlines():
		time.sleep(0.05)
		print(sidra)


def instaup ():
	os.system('clear');baner()
	token = input('%s(%s⌯%s)%s TOKEN : %s'%(C,E,C,C,E))
	ID = input('%s(%s⌯%s)%s ID Tele : %s'%(C,E,C,C,E))
	os.system('clear');baner()
	files = input('%s(%s⌯%s)%s FILE ID %s:%s'%(C,E,C,C,A,E))
	userss = len(open(files,'r').read().splitlines())
	print('%s(%s⌯%s)%s number %s:%s%s'%(C,E,C,C,A,E,userss))
	print (50 * '\033[1;92m~')
	
	file = open(files,'r')
	ok = 0
	while True:
		userid = file.readline().split('\n')[0] 
		if userid=="":
			print ('%s The examination has been completed.'%(C))
			break
		
		url = 'https://checker-up.herokuapp.com/?oid={}&submit=submit'.format(userid)
		headers = {
       'Host': 'checker-up.herokuapp.com',
       'Connection': 'keep-alive',
       'Cache-Control': 'max-age=0',
       'sec-ch-ua': 'Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
       'sec-ch-ua-mobile': '?1',
       'sec-ch-ua-platform': 'Android',
       'X-Chrome-offline': 'persist=0 reason=reload',
       'Upgrade-Insecure-Requests': '1',
       'User-Agent': str(generate_user_agent()),
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
       'Sec-Fetch-Site': 'none',
       'Sec-Fetch-Mode': 'navigate',
       'Sec-Fetch-User': '?1',
       'Sec-Fetch-Dest': 'document',
       'Accept-Encoding': 'gzip',
       'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7'}
		responsa = requests.get(url,headers=headers).text
		if ('main') in responsa:
			ok+=1
			print('%s(%s%s%s)%s %s %s|%s False'%(C,E,str(ok),C,C,userid,E,C))
			
			
		elif ('{"coins":') in responsa:
			coinx = str(responsa.split('coins":"')[1])
			coin = str(coinx.split('"')[0])
			if int(coin) >800:
				ok+=1
				print('%s(%s%s%s)%s %s %s|%s %s'%(C,E,str(ok),C,E,userid,A,E,coin))
				massage=("• Successful Coins UP ⌯\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\n[💠] ID  : "+str(userid)+"\n[💰] Coins  : "+str(coin)+"\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nTele ⌯• @HrHrr")
				requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(massage))
				open('coins-800.txt','a').write(str(userid)+"\n")
				
			elif int(coin) >400 and int(coin) < 800:
				ok+=1
				print('%s(%s%s%s)%s %s %s|%s %s'%(C,E,str(ok),C,E,userid,A,E,coin))
				massage=("• Successful Coins UP ⌯\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\n[💠] ID  : "+str(userid)+"\n[💰] Coins  : "+str(coin)+"\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nTele ⌯• @HrHrr")
				requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(massage))
				open('coins-400.txt','a').write(str(userid)+"\n")
				
			else:
				ok+=1
				print('%s(%s%s%s)%s %s %s|%s %s'%(C,E,str(ok),C,H,userid,A,H,coin))
			
		
		else:
			ok+=1
			print('%s(%s%s%s)%s %s %s|%s False'%(C,E,str(ok),C,C,userid,E,C))
		
		
instaup()
    
