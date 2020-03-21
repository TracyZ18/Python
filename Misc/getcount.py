# get webpage content as bytes (UTF-8)
# convert to string 
import urllib.request
fp = urllib.request.urlopen("https://www.quebec.ca/en/health/health-issues/a-z/2019-coronavirus/situation-coronavirus-in-quebec/")
pagebytes = fp.read()
page = pagebytes.decode("utf8")
fp.close()

# get count
index = page.find("<strong>Québec</strong>")
page = page[index+23:index+53]
numstr = ''.join(x for x in page if x.isdigit())

# construct csv string to append
from datetime import datetime
csv_str = "\n"+datetime.today().strftime('%m-%d')+","+numstr

# get latest count in record
cur = open('covid-19.csv', 'r') 
cur_lines = cur.readlines() 
cur_record = cur_lines[-1]
cur_record = cur_record[cur_record.find(",")+1:]

# only append if a new count is obtained 
if int(cur_record) is not int(numstr) :
    with open('covid-19.csv','a') as fd:
        fd.write(csv_str)
else :
    exit()

# make a new graph if new count appended
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("covid-19.csv", names=["DATE","COUNT"])
df.plot.scatter(x='DATE',y='COUNT')
plt.savefig('covid-19.png')