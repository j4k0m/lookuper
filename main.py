#!/usr/bin/python3
import requests, json, sys
from multiprocessing import Pool


def check(i):
    i = i.strip("\n")
    _i = i.split("/")[0]
    json_data = json.loads(requests.get(URL.format(_i)).text)
    with open("./result.txt", "a+") as result:
        fr = f"{i}, {json_data['country']}, {json_data['city']}"
        result.write(fr + "\n")
        result.close()
        print(fr)

URL = "https://ipwhois.app/json/{}"

if __name__ == '__main__':
    with Pool(50) as c:
        c.map(check, open(sys.argv[1], "r").readlines())
