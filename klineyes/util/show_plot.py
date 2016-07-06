import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.gridspec import GridSpec

def mfi(df):
    df['date'] = pd.to_datetime(df.date)

    fig = plt.figure(figsize=(16, 9))
    gs = GridSpec(3, 1) # 2 rows, 3 columns
    fig.suptitle(df['date'][-1:].values[0])
    fig.set_label('MFI')
    price = fig.add_subplot(gs[:2, 0])
    price.plot(df['date'], df['close'], color='blue')

    indicator = fig.add_subplot(gs[2, 0], sharex=price)
    indicator.plot(df['date'], df['mfi'], c='pink')
    indicator.plot(df['date'], [20.]*len(df['date']), c='green')
    indicator.plot(df['date'], [80.]*len(df['date']), c='orange')

    price.grid(True)
    indicator.grid(True)
    plt.tight_layout()
    plt.show()
