# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 23:32:10 2018

@author: irenezyx
"""

import matplotlib.pyplot as plt
import mpld3
from mpld3 import plugins
import pandas as pd

buildings = pd.read_csv("IL_Building_Inventory.csv",
                       na_values = {'Year Acquired':0, 
                                    'Year Constructed':0, 
                                    'Square Footage':0,
                                    'Agency Name': 'Missed Value', 
                                    'Congress Dict': 'Missed Value'
                                    }
                       )

fig, ax = plt.subplots()
x = buildings['Year Acquired']
y = buildings['Year Constructed']
plt.xlabel('Year Acquired')
plt.ylabel('Year Constructed')
plt.title('Year Constructed VS. Year Acquired by Matplotlib')

labels = []
for i in range(len(x)):
    label = buildings[['Year Acquired', 'Year Constructed']].loc[3].to_frame()
    label.columns = ['Row {0}'.format(i)]
    # .to_html() is unicode; so make leading 'u' go away with str()
    labels.append(str(label.to_html()))

plots = ax.plot(x, y, 'o')

tooltip = plugins.PointHTMLTooltip(plots[0], labels=labels,
                                   voffset=10, hoffset=10)
plugins.connect(fig, tooltip)

mpld3.show()