#!/usr/bin/python3
import requests, json, sys

URL = "https://ipwhois.app/json/{}"

for i in open(sys.argv[1], "r").readlines():
    i = i.strip("\n")
    _i = i.split("/")[0]
    json_data = json.loads(requests.get(URL.format(_i)).text)
    with open("./result.txt", "a+") as result:
        fr = f"{i}, {json_data['country']}, {json_data['city']}"
        print(fr)
        result.write(fr + "\n")
        result.close()
