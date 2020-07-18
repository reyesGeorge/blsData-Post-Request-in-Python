import json
import requests
import csv
import time



headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['CUUR0000SA0', 'SUUR0000SA0'], "startyear": "2011", "endyear": "2014"})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)

print(json_data)

def get_data(json_data):
    start = time.perf_counter()
    for series in json_data['Results']['series']:
        x = csv.writer(open("test.csv", "w"))
        x.writerow(["series id", "year", "period", "value", "footnotes"])
        seriesId = series['seriesID']
        for item in series['data']:
            year = item['year']
            period = item['period']
            value = item['value']
            footnotes = ""
            for footnote in item['footnotes']:
                if footnote:
                    footnotes = footnotes + footnote['text'] + ','
            if 'M01' <= period <= 'M12':
                # x.add_row([seriesId, year, period, value, footnotes[0:-1]])
                x.writerow([seriesId, year, period, value, footnotes[0:-1]])


        finish = time.perf_counter()
        print(f'Finished in {round(finish - start, 2)} second(s)')

get_data(json_data)
