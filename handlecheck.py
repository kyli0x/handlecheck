#!/usr/bin/env python3
import os
import requests

# colors
W  = '\033[0m'  # white (default)
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan

username = ''

def checker(url):
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if r.status_code == 200:
        return True
    return False

def github(handle):
    url = 'https://github.com/' + handle
    return checker(url)

def instagram(handle):
    url = 'https://www.instagram.com/' + handle
    return checker(url)

def medium(handle):
    url = 'https://medium.com/@' + handle
    return checker(url)

def minecraft(handle):
    url = 'https://www.mc-heads.net/minecraft/profile/' + handle
    return checker(url)

def pastebin(handle):
    url = 'https://pastebin.com/u/' + handle
    return checker(url)

def reddit(handle):
    url = 'https://reddit.com/user/' + handle
    return checker(url)

def tryhackme(handle):
    url = 'https://tryhackme.com/p/' + handle
    return checker(url)

def twitch(handle):
    url = 'https://twitch.tv/' + handle
    return checker(url)

def twitter(handle):
    url = 'https://www.twitter.com/' + handle
    return checker(url)

def youtube(handle):
    url = 'https://www.youtube.com/user/' + handle
    return checker(url)

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
    username = input(C+' Type ['+P+'exit'+C+'] to close the program\n \n Enter a username to search:\n \n > '+W)
    if username == 'exit':
        exit()
    else:
        print('')
        print(W+'Github:    '+C+'' + (''+P+'Unavailable' if github(username) else ''+P+'Available'))
        print(W+'Instagram: '+C+'' + (''+P+'Unavailable' if instagram(username) else ''+P+'Available'))
        print(W+'Medium:    '+C+'' + (''+P+'Unavailable' if medium(username) else ''+P+'Available'))
        print(W+'Minecraft: '+C+'' + (''+P+'Unavailable' if minecraft(username) else ''+P+'Available'))
        print(W+'Pastebin:  '+C+'' + (''+P+'Unavailable' if pastebin(username) else ''+P+'Available'))
        print(W+'Reddit:    '+C+'' + (''+P+'Unavailable' if reddit(username) else ''+P+'Available'))
        print(W+'TryHackMe: '+C+'' + (''+P+'Unavailable' if tryhackme(username) else ''+P+'Available'))
        print(W+'Twitch:    '+C+'' + (''+P+'Unavailable' if twitch(username) else ''+P+'Available'))
        print(W+'Twitter:   '+C+'' + (''+P+'Unavailable' if twitter(username) else ''+P+'Available'))
        print(W+'YouTube:   '+C+'' + (''+P+'Unavailable' if youtube(username) else ''+P+'Available'))
        print('\n')
        main()
banner()
main()

