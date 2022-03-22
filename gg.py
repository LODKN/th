import requests,os
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
os.system('clear')
def whispers():
 for Whisper in open('id.txt','r').read().splitlines():
  id=str(Whisper.split('\n')[0])
  whisper = requests.get(f'http://35.181.7.112/check.php?oid={id}&submit=submit').text
  if 'coins":"' in whisper:
   Whisper = whisper.split('coins":"')[1]
   coin = Whisper.split('"')[0]
   print(f'{G}[✓] {id} Coins ==> {B}{coin}')
   if int(coin) > 600:
    with open('400-coins.txt','a') as f8:
     f8.write(id+' | '+coin+'\n')
  else:
   print(f'{E}[×] {id} ==> {S}ERROR')
whispers()
