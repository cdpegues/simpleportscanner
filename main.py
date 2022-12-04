#!usr/bin/Python3

#creds to https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_network_scanner.htm

#imports
from os import name
import socket
import time

#Main
if name == '_main_':
        target = input('Enter the host to be scanned')
        IP = socket.gethostname(target)
        print ('Starting scan on host: ', IP)

        for i in range (50, 500):
            s = socket(socket.AF_INET, socket.SOCK_STREAM)

            conn = s.connect_ex((IP, i))
            if(conn ==0): 
                print('Port %d: OPEN' % (i,))
            s.close()
print('Time taken:', time.time())
