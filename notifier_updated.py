#!/usr/bin/env python
# coding: utf-8

# In[4]:


from datetime import datetime
import time
from plyer import notification
import json
from time import sleep

file = r"timetable.json"

while(True):
    with open(file, 'r') as j:
        contents = json.load(j)

    now = datetime.now()
    current_time = now.strftime("%H:%M")

    for i in contents.items():
        if i[0] == datetime.now().strftime("%A"):
            for j in range(len(i[1])):
                time = list(i[1][j].values())
                if current_time == time[0]:
                    notification.notify(
                    title = "Subject: {}".format(*i[1][j].keys()),
                    message = "plz join. \nTime: {}".format(*i[1][j].values()),
                    app_icon = r"C:\Users\HP\Downloads\book.ico",
                    timeout=20
                )
    sleep(30)


# In[ ]:




