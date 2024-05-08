import argparse
import requests
import re


def crawlForLinks(url):
    print(f"[*] Crawling {url}")

    page = requests.get(url)

    maching = re.findall(r'href="(.*?)"', page.text)
    for link in maching:
        print(link)


def main():
    parser = argparse.ArgumentParser(
        description="List all links found in a web page"
    )
    parser.add_argument("url", type=str, help="The URL of the webpage")
    baseUrl = parser.parse_args().url
    crawlForLinks(baseUrl)


if __name__ == "__main__":
    main()
