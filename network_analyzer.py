import socket
import requests
import sys
import colorama
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored
import threading
from rich.progress import track
from time import sleep
from banner import * 
import scapy.all as scapy

print(Fore.LIGHTMAGENTA_EX+banner_art)
#print(colored('Hello, World!', 'green', 'on_red'))

print('\n')

print("1.Port Scanner\n")
print("2.Wifi Scanner\n")

choice = int(input(Fore.GREEN+'ENTER YOUR CHOICE :'))

#banner = banner_art

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 0


#This function scans the given host (for example: www.google.com) and display's the port's status.

def port_scanner():
    try:
        #host = str(input("ENTER THE HOST NAME:"))
        ip_addr = socket.gethostbyname(host)
        msg = (f"scanning the network {ip_addr}")
        for step in track(range(100), description=msg):
            sleep(0.1)
        for port in range(1,100):
            conn = s.connect_ex((ip_addr,port))
            if(conn==0):
                print(Fore.GREEN+f"port {port} is open",'on_green')
            else :
                print(Fore.RED+f"port {port} is not open")    
       
    
    except socket.gaierror:
        print("Enter the correct host !")
        sys.close()


#This function scan's your router and display's the connected devices.

def wifi_scanner():
    request = scapy.ARP() #Creating ARP packet using ARP() function.
        
    request.pdst = req
    msg = (f"Scanning network {request.pdst}")
    for step in track(range(100), description=msg):
            sleep(0.1)
    broadcast = scapy.Ether() #Creating Ether packet using Ether() function.
        
    broadcast.dst = 'ff:ff:ff:ff:ff:ff' #Destination set !
        
    request_broadcast = broadcast / request #Framing ethernet packet and arp packet using / .    clients = scapy.srp(request_broadcast, timeout = 10,verbose = 1)[0]
    
    for element in clients:
        print(element[1].psrc + "	 " + element[1].hwsrc)


if(choice==1):
    host = str(input(Fore.GREEN+"ENTER THE HOST NAME:"))
    port_scanner()

elif(choice==2):
    req = str(input(Fore.GREEN+"ENTER YOUR NETWORK RANGE :")) #Enter your router range (for example: 255.255.255.0/24) like this.
    wifi_scanner()

else:
    print(Fore.RED+"Error")
