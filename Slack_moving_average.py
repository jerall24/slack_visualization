#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
from datetime import datetime
from data_prep import data

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
months_fmt = mdates.DateFormatter('%B')
years_fmt = mdates.DateFormatter('%Y')



# In[3]:


# data = pd.read_csv("data.csv")
d = data[['Date','Daily members posting messages','Messages posted by members']]
d['Date'] = pd.to_datetime(d['Date'])
d['Date']


# In[4]:


ma = d.rolling(30, min_periods=1).mean()
d[["MA Members Posting","MA Messages Posted"]] = ma


# In[19]:


fig, ax = plt.subplots()
ax.plot_date(d['Date'], d['Messages posted by members'], "--", xdate=True, linewidth=1.5)
ax.plot_date(d['Date'], d['MA Messages Posted'], "-", xdate=True, linewidth=3,)
ax.plot_date(d['Date'][len(d)-1], d['MA Messages Posted'][len(d)-1], xdate=True, marker='x')
# ax.annotate(d['MA Messages Posted'][len(d)-1], xy=(d['Date'][len(d)-1],d['MA Messages Posted'][len(d)-1]))

# Goal here to is get the markers at every month

# format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)

ax.xaxis.set_minor_locator(months)
ax.xaxis.set_minor_formatter(months_fmt)

ticks = np.array(ax.get_xticks(minor=True))
# print(ticks)
for tick in ticks:
    loc = min(max(0, tick-18109), len(d)-1)
    ax.annotate(round(d['MA Messages Posted'][loc]), xy=(d['Date'][loc], d['MA Messages Posted'][loc]), verticalalignment='top', fontweight='semibold')

# round to nearest years.
datemin = np.datetime64(d['Date'][0], 'M')
datemax = np.datetime64(d['Date'][len(d)-1], 'M') + np.timedelta64(1, 'M')
ax.set_xlim(datemin-1, datemax+1)

# format the coords message box
ax.format_xdata = mdates.DateFormatter('%Y-%M')
ax.grid(True)

# rotates and right aligns the x labels, and moves the bottom of the
# axes up to make room for them
# fig.autofmt_xdate()

fig.set_figwidth(20)
fig.set_figheight(10)
ax.set_title("Moving Average of Slack posts by members in MCIT In-Person")
ax.set_ylabel("Messages Sent")
ax.set_xlabel("Date")
plt.savefig(f"output_images/MA Slack Messages All Time ({datetime.strftime(datetime.today(), '%m%d%Y')}).jpg")
plt.show()


# In[ ]:





# In[6]:


before_date = 420 # 2020-09-16
print(d.loc[0])
print(d.loc[before_date])
print(d.loc[len(d)-1])
before = d.loc[before_date]["MA Messages Posted"]
after = d.loc[len(d)-1]["MA Messages Posted"]
print((after-before)/before)


# In[ ]:




