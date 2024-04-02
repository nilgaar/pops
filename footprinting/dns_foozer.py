from enum import Enum
import dns.resolver, dns.reversename
import sys
import re


class DNSRecord(Enum):
    A = "A"
    AAAA = "AAAA"
    CNAME = "CNAME"
    MX = "MX"
    NS = "NS"
    PTR = "PTR"
    SOA = "SOA"
    TXT = "TXT"


entryPoint = sys.argv[1]
fuzzed = []


def runQuery(domain: str, record: DNSRecord) -> dns.resolver.Answer:
    try:
        return dns.resolver.resolve(domain, record)
    # https://dnspython.readthedocs.io/en/latest/exceptions.html#module-dns.exception
    except Exception as e:
        print(f"Exception: {record}: {e}")
        return None


def queryFor(domain):
    for record in DNSRecord:
        r = runQuery(domain, record.value)
        # if record is DNSRecord.A or record is DNSRecord.AAAA:
        if r:
            print(f"{record.name}: {r.nameserver}")

    # Add an indented block of code here
    # for record in DNSRecord:
    #     # try:
    #         answers = dns.resolver.resolve(entryPoint, record.value)
    #         print(answers)
    #         for rdata in answers:
    #             try:
    #                 x=re.search("\b([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}\b", rdata.address)
    #                 print(x.start())
    #                 print(f'{record.name}: {rdata}')
    #             except Exception as e:
    #                 print(f'2:::::::{record.name}: {e}')
    #             print('x::::')

    #     # except Exception as e:
    #     #     print(f'{record.name}: {e}')


queryFor(entryPoint)
