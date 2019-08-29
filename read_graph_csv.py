# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:51:55 2019

@author: chandlerzach
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sns


def heat_map(input_data_frame):
  rwb = colors.ListedColormap(["blue","white", "red"])
  plt.figure(figsize=(11,11))
  ax = sns.heatmap(input_data_frame, vmin=-0.4, vmax=1.5, cmap=rwb, annot=True, fmt=".1f", square=True, cbar_kws={"shrink": .8})
  ax.invert_yaxis()
  ax.invert_xaxis()
  ax.xaxis.tick_top()
  ax.yaxis.tick_left()
  ax.xaxis.set_label_position("top")
  plt.show()
  plt.close()

if __name__ == "__main__":

  sns.set()
  num_syllables = 19
  df = pd.read_csv("simtestdata.csv", converters={"Index": lambda x: str(x),"Syllable": lambda x: int(x)})
  sdf = pd.read_csv("senft2016data.csv", index_col="Label")
  df.set_index("Index", inplace=True)
  data = df.drop(columns="Trial")
  means = (df.groupby("Index")["Syllable"].mean()) / num_syllables
  
  print(f'The mean of the means of our mean data set is {means.mean():.4f} and the standard deviation {means.std():.4f}')
  
  list_lg, list_le = [list(), list()]
  for i in means.index:
      list_lg.append(i[0:2])
      list_le.append(i[2:5])
  
  frame = {"syl_means": means.values, "lg": list_lg, "le": list_le}
  warm_data = pd.DataFrame(frame).pivot_table(values="syl_means", index="lg", columns="le")
  heat_map(warm_data)
