import sys
from collections import Counter
from client import BaseClient
import requests
from friends import get_age, GetFriends, GetUser

import matplotlib.pyplot as plt
import numpy as np


a = GetUser('id44014204')
b = a.execute()
us1 = b.json()
us_id = us1['response'][0]['uid']
print(us_id)
j = 0
res = []
friends_list = GetFriends(us_id)
bb = friends_list.execute()
friends = bb.json()  # массив словарей

for i in range(len(friends['response'])):
    if ('bdate' in friends['response'][i] and len(friends['response'][i]['bdate'].split('.')) == 3):
        res.append(get_age(friends['response'][i]['bdate'].split('.')))

res1 = Counter(res)
data1 = res1
ages = []
for i in list(res1):
    ages.append(res1[i])

locs = ages
plt.grid()
plt.minorticks_on()
plt.axis([0, 120, 0, 50])
plt.figure(num=1, figsize=(8, 6))
plt.xlabel('age', size=14)
plt.ylabel('count', size=14)
plt.bar(data1, locs, width=0.5)
plt.show()

