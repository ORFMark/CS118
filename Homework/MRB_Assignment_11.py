import csv
import re
regex=re.compile("^1|^2")
markets={}
with open('Text Stuff/markets.csv',newline='') as f:
    reader=csv.DictReader(f)
    for row in reader:
        if regex.search(row['zip']):
            if row['zip'] not in markets.keys():
                markets[row["zip"]]=[row["MarketName"]]
            else:
                markets[row["zip"]].append(row["MarketName"])
zips=sorted(markets.keys())
for i in zips:
    print("The markets in the",i, "zip code area are",markets[i])
