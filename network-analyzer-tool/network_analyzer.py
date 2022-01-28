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

print(Fore.LIGHTMAGENTA_EX+banner_art)
#print(colored('Hello, World!', 'green', 'on_red'))


#banner = banner_art

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 0


#t1 = threading.Thread(target=print_square, args=(10,))


try:
    host = str(input("ENTER THE HOST NAME:"))
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

