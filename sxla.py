import optparse
import requests
import sys
import time
def slowprint(s):
	for c in s :
      	   sys.stdout.write(c)
      	   sys.stdout.flush()
           time.sleep(5. / 100)
slowprint("[/]SXLA Scanner v1.0[/]\nDeveloped by Unknown Tinkers\n\n")
parser=optparse.OptionParser("usage "+"-s <SQLI> or -x <XSS> or -l <LFI> or -a <Admin Finder>\n")
print("example:sxlscanner.py -s <Target Website>\n")
parser.add_option('-s',dest='sqli',type='string',help='specify attack type')
parser.add_option('-x',dest='xss',type='string',help='specify attack type')
parser.add_option('-l',dest='lfi',type='string',help='specify attack type')
parser.add_option('-a',dest='admin',type='string',help='specify attack type')
(options,arg)=parser.parse_args()
if(options.sqli==None)&(options.xss==None)&(options.lfi==None)&(options.admin==None):
	print (parser.usage)
	exit(0)
if options.sqli!=None:
	target=options.sqli
	response=requests.get(target+"'").text
	if 'error' in response and 'syntax' in response or 'MySQL' in response or "QUERY" in response:
		slowprint("Target is vulnerable to SQLInjection\n")
	else:
		slowprint("Its not vulnerable")
if options.lfi!=None:
	target=options.lfi
	with open('lfi.txt','r') as f:
		f=f.readlines()
		for i in range(len(f)):
			payload=f[i].strip('\n')
			response=requests.get(target+payload).text
			print target+payload
			if '/bin/bash' in response or 'www-data:/var/www' in response:
				slowprint("Its vulnerable to LFI : "+target+payload+'\n')
				break
if options.admin!=None:
	target=options.admin
	with open('admins.txt','r') as f:
		f=f.readlines()
		for i in range(len(f)):
			payload=f[i].strip('\n')
			response=requests.get(target+'/'+payload)
			if response.status_code==200:
				slowprint("[+]Found admin panel : "+target+'/'+payload+'\n')
if options.xss!=None:
	target=options.xss
	with open('xss.txt','r') as f:
		f=f.readlines()
		for i in range(len(f)):
			payload=f[i].strip('\n')
			response=requests.get(target+payload).text
			if payload in response:
				slowprint("[+]Vulnerable to XSS : "+target+payload+'\n')

