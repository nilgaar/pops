import argparse
import requests
import re

alreadyCrawled = {""}


def crawlForLinks(url):
    print("baseUrl:", baseUrl)
    alreadyCrawled.add(url)
    print(f"[*] Crawling {url}")

    page = requests.get(url)
    mach = re.findall(r'href="(.*?)"', page.text)

    for link in mach:
        print(link)
        if baseUrl in link and link not in alreadyCrawled:
            crawlForLinks(link)


def main():
    global baseUrl
    parser = argparse.ArgumentParser(description="List all links found in a web page")
    parser.add_argument("url", type=str, help="The URL of the webpage")
    baseUrl = parser.parse_args().url
    crawlForLinks(baseUrl)


if __name__ == "__main__":
    main()
