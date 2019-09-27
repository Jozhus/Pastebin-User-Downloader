import urllib.request, os
from bs4 import BeautifulSoup as bs

def getLinks(user):
    html = urllib.request.urlopen("https://pastebin.com/u/" + user).read().decode('utf-8')
    stuff = bs(html, "html.parser").find_all("table", class_="maintable")[0].find_all('a')
    return [(x.get("href"), x.get_text()) for x in stuff[::2]]

def copyRaw(ext):
    html = urllib.request.urlopen("https://pastebin.com/raw" + ext).read().decode('utf-8')
    return bs(html, "html.parser").get_text()

def download(ext, name):
    global user
    path = "Pastebin/" + user
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.isfile(path + '/' + name + '.txt'):
        print("Downloading " + name)
        file = open(path + '/' + name + '.txt', 'w')
        file.write(copyRaw(ext))
        file.close()

if __name__ == "__main__":
    user = input("User: ")
    for x in getLinks(user):
        download(x[0], x[1])
    print("Done!")
