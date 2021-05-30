#!/usr/bin/env python3
import os
import yaml
import requests

# colors
W  = '\033[0m'  # white (default)
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan
    

def checker():
    handle = input(C+' Type ['+P+'exit'+C+'] to close the program\n \n Enter a username to search:\n \n > '+W)
    if handle == 'exit':
        exit()
    else:
        with open('websites.yml') as f:
            data = yaml.safe_load(f)
            links = data['sites']

        weblinks = ["{}{}".format(i,handle) for i in links]

        for url in weblinks:
            r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            if r.status_code == 200:
                print(C+'Unavailable for: '+W+'' + url)
            else:
                print(C+'Available for:   '+W+'' + url)
        main()



def banner():
    try:
        os.system('cls')
        raise ValueError('Error')
    except Exception:
        os.system('clear')
    print (C+'')
    print ('  ██░ ██  ▄▄▄       ███▄    █ ▓█████▄  ██▓    ▓█████ ')
    print (' ▓██░ ██▒▒████▄     ██ ▀█   █ ▒██▀ ██▌▓██▒    ▓█   ▀ ')
    print (' ▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌▒██░    ▒███   ')
    print (' ░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌▒██░    ▒▓█  ▄ ')
    print (' ░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒████▓ ░██████▒░▒████▒')
    print ('  ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░ ▒░▓  ░░░ ▒░ ░')
    print ('  ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒ ░ ░ ▒  ░ ░ ░  ░')
    print ('  ░  ░  ▄████▄ ░ ██░ ██ ▓█████  ▄████▄   ██ ▄█▀ ')
    print ('       ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ')      
    print ('       ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ')      
    print ('       ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ')      
    print ('       ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄ ')     
    print ('       ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒  ')    
    print ('         ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ')     
    print ('                 ░  ░░ ░   ░            ░  ░ ░ ')      
    print ('                     ░                     ░   ')        
    print (C+' '+C+' Created by: Kyli0x')
    print (P+'  GitHub: ['+C+'kyli0x'+P+']')
    print (P+'  Insta:  ['+C+'kyli0x'+P+']')
    print ('')

def main():
    checker()

banner()
main()