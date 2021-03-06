# get webpage content as bytes (UTF-8)
# convert to string 
import urllib.request
fp = urllib.request.urlopen("https://www.quebec.ca/sante/problemes-de-sante/a-z/coronavirus-2019/situation-coronavirus-quebec/")
pagebytes = fp.read()
page = pagebytes.decode("utf8")
fp.close()

# get date, exit if not today
index = page.find("Nombre de cas confirmés, en date")
date_str = page[index+35:index+40]
date_str = ''.join(x for x in date_str if x.isdigit())
if len(date_str) == 1 :
    date_str = "0" + date_str
from datetime import datetime
today = datetime.today().strftime('%d')
if date_str != today :
    print(date_str)
    exit()

# get count
index = page.find("<strong>Au Québec</strong>")
segment = page[index+30:]
num_str = segment[:30]
num_str = ''.join(x for x in num_str if x.isdigit())\

# get death
index = segment.find("dont")
segment = segment[index:]
death_str = segment[:30]
death_str = ''.join(x for x in death_str if x.isdigit())

# get Montreal
index = segment.find("06 - Montréal")
segment = segment[index+30:]
mtl_str = segment[:30]
mtl_str = ''.join(x for x in mtl_str if x.isdigit())

# function to append record
def append(filename, record) :
    # construct csv string to append
    csv_str = "\n"+datetime.today().strftime('%m-%d')+","+record

    # get latest in file
    cur = open(filename, 'r') 
    cur_lines = cur.readlines()
    if cur_lines :
        cur_record = cur_lines[-1]
    else :
        csv_str = csv_str[1:]
        cur_record = ''
    
    # no record, use previous record
    if not record :
        csv_str += cur_record[6:]

    # only append if a new count is obtained
    if ("\n" + cur_record) != csv_str :
        with open(filename,'a') as fd:
            fd.write(csv_str)
        return True # appended
    return False # not appended

# append new record to each file
appended = append('covid-19.csv',num_str)
appended = append('death.csv',death_str) or appended
appended = append('montreal.csv',mtl_str) or appended

def graph() :
    # make a new graph
    import pandas as pd
    import matplotlib.pyplot as plt
    df = pd.read_csv("covid-19.csv", names=["DATE","COUNT"])
    df.plot.scatter(x='DATE',y='COUNT')
    plt.savefig('covid-19.png')
    mtl = pd.read_csv("montreal.csv", names=["DATE","COUNT"])
    mtl.plot.scatter(x='DATE',y='COUNT')
    plt.savefig('covid-19-montreal.png')

# only graph if new data appended
if appended :
    graph()