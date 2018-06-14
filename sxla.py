import optparse
import requests
import socket
import sys
import urllib
print ("""


  ██████ ▒██   ██▒ ██▓    ▄▄▄      
▒██    ▒ ▒▒ █ █ ▒░▓██▒   ▒████▄    
░ ▓██▄   ░░  █   ░▒██░   ▒██  ▀█▄  
  ▒   ██▒ ░ █ █ ▒ ▒██░   ░██▄▄▄▄██ 
▒██████▒▒▒██▒ ▒██▒░██████▒▓█   ▓██▒
▒ ▒▓▒ ▒ ░▒▒ ░ ░▓ ░░ ▒░▓  ░▒▒   ▓▒█░
░ ░▒  ░ ░░░   ░▒ ░░ ░ ▒  ░ ▒   ▒▒ ░
░  ░  ░   ░    ░    ░ ░    ░   ▒   
      ░   ░    ░      ░  ░     ░  ░
                                   

\n
[+][+][+]Developed by Unknown Tinkers[+][+][+]\n
[+][+][+]Released Date 5/30/2018[+][+][+] \n""")
parser=optparse.OptionParser("usage "+"-s <SQLI> or -x <XSS> or -l <LFI>")
print("example:sxlscanner.py -s")
parser.add_option('-s',dest='sname',type='string',help='specify attack type')
parser.add_option('-x',dest='xname',type='string',help='specify attack type')
parser.add_option('-l',dest='lname',type='string',help='specify attack type')
(options,arg)=parser.parse_args()
if(options.sname==None)&(options.xname==None)&(options.lname==None):
	print (parser.usage)
	exit(0)
if(options.sname!= None):
	target=input("Enter URL to attack with SQLI(eg http://www.google.com):")
	response=requests.get(target+"'").text
	if 'error' in response and 'syntax' in response or 'MySQL' in response:
		print ("Its vulnerable to SQLInjection")
	else:
		print ("Its not vulnerable")
if(options.xname!=None):
	target=input("Enter url to test XSS:")
	with open("xss.txt","r") as f:
		for line in f:
			param=line.strip('\n')
			host=target+param
			print ("Checking website "+target+param+'\n')
if(options.lname!=None):
	target=input("Enter LFI url:")



