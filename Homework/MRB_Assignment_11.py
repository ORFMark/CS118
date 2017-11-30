import csv
import re
regex=re.compile("^1|^2")
with open('Text Stuff/markets.csv',newline='') as f:
    reader=csv.DictReader(f)
    for row in reader:
        if regex.search(row['zip']):
            print(row['MarketName'],row['zip'])
    
