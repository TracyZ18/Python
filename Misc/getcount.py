# get webpage content as bytes (UTF-8)
# convert to string 
import urllib.request
fp = urllib.request.urlopen("https://www.quebec.ca/sante/problemes-de-sante/a-z/coronavirus-2019/situation-coronavirus-quebec/")
pagebytes = fp.read()
page = pagebytes.decode("utf8")
fp.close()

# get count
index = page.find("<strong>Au Québec</strong>")
segment = page[index+23:]
num_str = segment[:30]
num_str = ''.join(x for x in num_str if x.isdigit())

# get death
index = segment.find("dont")
segment = segment[index:]
death_str = segment[:30]
death_str = ''.join(x for x in death_str if x.isdigit())

# get recovered 
index = segment.find("personnes décédées")
segment = segment[index:]
recovered_str = segment[:30]
recovered_str = ''.join(x for x in recovered_str if x.isdigit())

# get Montreal
index = segment.find("06 - Montréal")
segment = segment[index+30:]
mtl_str = segment[:30]
mtl_str = ''.join(x for x in mtl_str if x.isdigit())

# function to append record
def append(filename, record) :
    # construct csv string to append
    from datetime import datetime
    csv_str = "\n"+datetime.today().strftime('%m-%d')+","+record

    # get latest in file
    cur = open(filename, 'r') 
    cur_lines = cur.readlines()
    if cur_lines :
        cur_record = cur_lines[-1]
    else :
        csv_str = csv_str[1:]
        cur_record = ''

    # only append if a new count is obtained
    if cur_record != datetime.today().strftime('%m-%d')+","+record :
        with open(filename,'a') as fd:
            fd.write(csv_str)
        return True

# append new record to each file
appended = append('covid-19.csv',num_str)
appended = append('death.csv',death_str) or appended
appended = append('recovered.csv',recovered_str) or appended
appended = append('montreal.csv',mtl_str) or appended
if not appended :
    exit()

# make a new graph if new count appended
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("covid-19.csv", names=["DATE","COUNT"])
death = pd.read_csv("death.csv", names=["DATE","COUNT"])
recovered = pd.read_csv("recovered.csv", names=["DATE","COUNT"])

df.plot.scatter(x='DATE',y='COUNT')
plt.savefig('covid-19.png')

# make graph of active cases (in progress)
for x in range(len(death.index)) :
    df.at[x+11,'COUNT'] -= death.at[x,'COUNT']
    df.at[x+11,'COUNT'] -= recovered.at[x,'COUNT']

df.plot.scatter(x='DATE',y='COUNT')
plt.savefig('covid-19-active.png')

mtl = pd.read_csv("montreal.csv", names=["DATE","COUNT"])
mtl.plot.scatter(x='DATE',y='COUNT')
plt.savefig('covid-19-montreal.png')