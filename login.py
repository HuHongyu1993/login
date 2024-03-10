import os
import re
import json
import pyautogui as pag

username = "%s@example.com" % os.popen("echo %username%").read().rstrip()
password = "*"
position = (960, 518)
try:
    fin = open("username.json", "r")
    data = json.loads(fin.read())
    username = data['username']
    password = data['password']
    position = data['position']
    position = re.findall('\d+', position)
    position = tuple(position)
    fin.close()
except:
    print('use default account')

pag.click(position)
pag.write(username)
pag.press('tab')
if "*" in password:
    password = ""
else:
    pag.write(password)
    pag.press('tab')
    pag.press('tab')
    pag.press('enter')
