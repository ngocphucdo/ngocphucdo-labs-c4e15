from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
db = client.get_default_database()

customers = db ['customers']
customers_list = customers.find()

events = 0
wom = 0
ads = 0

for customers in customers_list:
    if 'events' == customers['ref']:
        events += 1
    elif 'wom' == customers['ref']:
        wom += 1
    elif 'ads' == customers['ref']:
        ads += 1

print('events=',events,'nguoi')
print('wom=',wom,'nguoi')
print('ads=',ads,'nguoi')

ets = (events * 100) / 6969
print('events=',ets,'%')
w0m = (wom * 100) / 6969
print('wom=',w0m,'%')
advers = (ads * 100) / 6969
print('ads',advers,'%')

#ve bieu do
from matplotlib import pyplot

labels = ['ads','wom','events']
values = [55.96, 16.22, 27.80]
colors = ['red','yellow','blue']

pyplot.pie(values, labels=labels, colors=colors, shadow = True)
pyplot.axis('equal')

pyplot.show()
