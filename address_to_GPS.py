# coding=UTF-8
import requests
import urllib
import json
import time

def get_latitude_longtitude(address):
    # decode url
    address = urllib.quote(address)
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + address + "&key=<Google API Key Here>"

    while True:
        res = requests.get(url)
        print res.text
        js = json.loads(res.text)

        if js["status"] != "OVER_QUERY_LIMIT":
            time.sleep(1)
            break

    result = js["results"][0]["geometry"]["location"]
    lat = result["lat"]
    lng = result["lng"]

    return lat, lng


with open("factory.csv","r") as my_csv:
    my_csv.readline()
    with open("result.csv","w") as result:
        x_list = [x.strip().split(",") for x in my_csv]
        i = 1
        for x in x_list:
            for elem in x:
                result.write(elem)
                print elem.encode()
                result.write(",")
            #lonlat = get_latitude_longtitude(x[3])
            #print lonlat
            #result.write(str(lonlat))
            result.write("\n")
            if i%5000 == 0:
                time.sleep(100)
                continue
