import logging
import requests
import threading
import os

url = "https://foursquare.com/user/"
headers = {
    "Cookie": "PixelDensity=1.25; bbhive=SGYOF1BP5PVHSLTIHQL41IBVTCS02N%3A%3A1741255239; OptanonConsent=isIABGlobal=false&datestamp=Tue+Mar+07+2023+17%3A00%3A52+GMT%2B0700+(Indochina+Time)&version=6.16.0&hosts=&consentId=a0677f84-e089-4425-b0a7-9cc6bae12add&interactionCount=1&landingPath=https%3A%2F%2Ffoursquare.com%2Fexplore%3Fmode%3Durl%26near%3DHanoi%252C%2520Th%25C3%25A0nh%2520Ph%25E1%25BB%2591%2520H%25C3%25A0%2520N%25E1%25BB%2599i%252C%2520Vietnam%26nearGeoId%3D72057594039509066&groups=C0005%3A1%2CC0004%3A1%2CC0003%3A1%2CC0002%3A1%2CC0001%3A1",
    "Sec-Ch-Ua": '" Not A;Brand";v="99", "Chromium";v="104"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
}


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")


file_handler = logging.FileHandler("crawl.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def crawl(start):
    for userID in range(start, start + 1000):
        output_file = os.path.join("root", "data", str(userID))
        with open(output_file, "w", encoding="UTF-8") as file:
            url1 = url + str(userID)
            response = requests.request("GET", url1, headers=headers)
            file.write(response.text)
        logger.info(url1)
    file.close()


if __name__ == "__main__":
    threads = []
    params_list = []
    for i in range(1, 11):
        params_list.append(i * 1000)
    for i in params_list:
        t = threading.Thread(target=crawl, args=(i,))
        threads.append(t)
        t.start()
    # Wait for all threads to finish
    for t in threads:
        t.join()
